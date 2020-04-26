from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from public.models import EarlyAccess


class EarlyAccessCreate(CreateView):
    template_name = 'public/index.html'
    model = EarlyAccess
    fields = ['email_address']
    success_url = reverse_lazy('public:thanks')

    def form_valid(self, form):
        return super().form_valid(form)
