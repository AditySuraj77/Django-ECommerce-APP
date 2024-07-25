
from django.urls import path
from ecommerceAuth import views

urlpatterns = [
    path('SignUp', views.SignUp,name="SignUp"),
    path('LogIn', views.LogIn,name="LogIn"),
    path('LogOut', views.LogOut,name="LogOut"),
]