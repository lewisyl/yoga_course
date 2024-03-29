from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logging_in/', views.logging_in, name='logging_in'),
    path('register/', views.register, name='register'),
    path('reg_form/', views.reg_form, name='reg_form'),
    path ('sign_in_user/', views.sign_in_user, name='sign_in_user'),
    path ('sign_out/', views.sign_out, name='sign_out'),
]