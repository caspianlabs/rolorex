from django.urls import path
from django.views.generic.base import TemplateView

from public.views import EarlyAccessCreate

app_name = 'public'
urlpatterns = [
    path('', EarlyAccessCreate.as_view(), name='index'),
    path('thanks', TemplateView.as_view(template_name='public/thanks.html'), name='thanks')
]
