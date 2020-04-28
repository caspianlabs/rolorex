from django.conf import settings
from django.urls import path, include

from registration.views import UserCreate, activate

app_name = 'registration'

if settings.FLAGS.ENABLE_REGISTRATION:
    urlpatterns = [
        path('', include('django.contrib.auth.urls')),
        path('register', UserCreate.as_view(), name='register'),
        path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate')
    ]
else:
    urlpatterns = [
        path('', include('django.contrib.auth.urls'))
    ]
