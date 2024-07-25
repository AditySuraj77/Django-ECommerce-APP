from django.contrib import admin
from django.urls import path
from ecommerceAPP import views

urlpatterns = [
    path('', views.home,name="home"),
    path('contact', views.contact,name="contact"),
    path('checkOut', views.CheckOut,name="CheckOut"),
    path('reset-password', views.Reset_Password,name="Reset_Password"),
]
