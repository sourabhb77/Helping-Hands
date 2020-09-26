from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register ,name='accounts-register'),
    path('about/', views.about ,name='accounts-about'),
    path('login/', views.login ,name='accounts-login'),
]
