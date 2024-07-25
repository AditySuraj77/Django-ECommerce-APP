from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from ecommerceAPP import views
# Create your views here.

def SignUp(request):
    if request.method == "POST":
        FullName = request.POST.get("fullname")
        email = request.POST.get("email")
        Password = request.POST.get("password")
        ConfirmPassword = request.POST.get("confirm_password")

        if User.objects.filter(username=email).exists():
            messages.warning(request,"Email Already Exists ! ")
            return redirect(SignUp)
        
        if User.objects.filter(email=email).exists():
            messages.info(request,"Email Already Exists ! ")
            return redirect(SignUp)
        
        if Password != ConfirmPassword:
            messages.error(request,"Password Not Match ! ")
            return redirect(SignUp)
        
        if len(Password) < 6 and len(ConfirmPassword) < 6:
            messages.error(request," Password must be greater than 6 ! ")
            return redirect(SignUp)

        user_created = User.objects.create(username=email,first_name=FullName,email=email)
        user_created.set_password(Password)
        user_created.save()
        messages.success(request,"SignUp Successfully. Now Login")
        return redirect(SignUp)
    return render(request,"signUp.html")


def LogIn(request):
    if request.method == "POST":
        email = request.POST.get("email")
        Password = request.POST.get("password")

        if not User.objects.filter(username=email).exists():
            messages.info(request,"Email Not Found !")
            return redirect(LogIn)
        user_log = authenticate(username=email,password=Password)

        if user_log is None:
            messages.error(request,"Incorrect Password")
            return redirect(LogIn)
        else:
            login(request,user_log)
            return redirect(views.home)
    return render(request,"login.html")

def LogOut(request):
    logout(request)
    messages.info(request,'You LogOut !')
    return redirect(LogIn)
