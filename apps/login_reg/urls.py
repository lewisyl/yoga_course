from django.urls import path
from . import views

urlpatterns = [
    path ('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path ('main_page/', views.main_page, name='main_page'),
    path ('sign_in_user/', views.sign_in_user, name='sign_in_user'),
    path ('sign_out/', views.sign_out, name='sign_out'),
]