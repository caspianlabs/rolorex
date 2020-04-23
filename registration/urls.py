from django.urls import path, include

from registration.views import UserCreate

app_name = 'registration'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', UserCreate.as_view(), name='register')
]
