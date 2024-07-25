from django.shortcuts import render, redirect,HttpResponse
from .models import Contact,Product
from django.contrib import messages
from ecommerceAuth.views import LogIn
from math import ceil
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.


def home(request):
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}
    
    return render(request,"home.html",params)


def contact(request):
    if not request.user.is_authenticated:
        messages.info(request,"Login for Contact us !")
        return redirect(LogIn)

    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("email")
        question = request.POST.get("question")
        query = Contact(Name=name,Email=email,Question=question)
        query.save()
        messages.info(request,"Thanks for Contact Us We will get you Soon...")
        return redirect(contact)


    return render(request,'contact.html')


def CheckOut(request):
    return render(request,"checkout.html")


def Reset_Password(request):
    if request.method == "POST":
        email_or_username = request.POST["emailORUsername"]
        new_password = request.POST["new_password"]
        confirm_new_password = request.POST["confierm_new_password"]

         # Validate email or username format
        if not (email_or_username.count('@') == 1 and '.' in email_or_username):
            messages.error(request, "Invalid email or username format")
            return redirect(Reset_Password)

        # validate password
        if new_password != confirm_new_password:
            messages.error(request,"Password Not Match ! ")
            return redirect(Reset_Password)

        user = get_object_or_404(User, username=email_or_username)
        try:                    
            if user:
                user.set_password(new_password)
                user.save()
                messages.success(request,"Password Updated. Try to Login")
                return redirect(Reset_Password)
            else:
                messages.info(request,"UserName or Email Wrong ! ")
                return redirect(Reset_Password)
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request,'reset_password.html')