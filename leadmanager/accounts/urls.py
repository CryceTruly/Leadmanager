from django.urls import path,include
from .api import RegistrationApi,LoginApi,UserApi

from knox import views as knox_views
urlpatterns=[
    path('api/auth',include('knox.urls')),
    path('api/auth/register',RegistrationApi.as_view()),
    path('api/auth/login',LoginApi.as_view()),
     path('api/auth/user',UserApi.as_view()),
      path('api/auth/logout',knox_views.LogoutView.as_view(),name='knox_logout')
    
]