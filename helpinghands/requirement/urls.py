from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("" , views.home, name= "admin-home"),
    path("home" , views.home2, name= "home"),

    path("new_listing" , views.fillListForm , name ="listing"),
    path("new_listings" , views.fillListForm , name ="login"),
    path("new_listings2" , views.fillListForm , name ="register"),
    path("new_listings3" , views.fillListForm , name ="logout")



]
