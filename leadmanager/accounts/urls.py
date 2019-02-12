from django.urls import path,include
from .api import RegistrationApi
from knox import views as knox_views
urlpatterns=[
    path('api/auth',include('knox.urls')),
    path('api/auth/register',RegistrationApi.as_view())
]