from django.urls import path, include

from registration.views import UserCreate
from rolorex.launchdarkly import ld, any_user

app_name = 'registration'

if ld.variation('registration_enabled', any_user, True):
    urlpatterns = [
        path('', include('django.contrib.auth.urls')),
        path('register', UserCreate.as_view(), name='register')
    ]
else:
    urlpatterns = [
        path('', include('django.contrib.auth.urls'))
    ]
