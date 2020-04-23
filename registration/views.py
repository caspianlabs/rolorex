from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import UserCreationForm


class UserCreate(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('public:index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
