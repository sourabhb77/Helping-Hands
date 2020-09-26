from django.contrib import admin
from django.urls import path
from .views import listingListView
from . import views


urlpatterns = [
    path("" , views.listingListView.as_view(), name= "admin-home"),
    path("home" , views.home, name= "home"),

    path("new_listing" , views.fillListForm , name ="listing"),
    path("new_listings" , views.fillListForm , name ="login"),
    path("new_listings2" , views.fillListForm , name ="register"),
    path("new_listings3" , views.fillListForm , name ="logout")
]



