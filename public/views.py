from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from public.models import EarlyAccess
from tasks.mail_task import send_email_task


class EarlyAccessCreate(CreateView):
    template_name = 'public/index.html'
    model = EarlyAccess
    fields = ['email_address']
    success_url = reverse_lazy('public:thanks')

    def form_valid(self, form):
        send_email_task.delay(
            [form.cleaned_data['email_address']],
            '[Rolorex] Early Acccess',
            'mail/early_access',
            {
                'email_address': [form.cleaned_data['email_address']]
            }
        )

        send_email_task.delay(
            # TODO use ADMINS
            ['team@caspianlabs.org'],
            '[Rolorex] New Early Access',
            'mail/admin_early_access',
            {
                'email_address': form.cleaned_data['email_address']
            }
        )

        return super().form_valid(form)
