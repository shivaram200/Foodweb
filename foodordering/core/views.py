from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from .models import Signup
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'foodord.html')
@login_required(login_url='login')
def services(request):
    return render(request,'services.html')
@login_required(login_url='login')
def aboutus(request):
    return render(request,'aboutus.html')
@login_required(login_url='login')
def contactus(request):
    return render(request,'contactus.html')
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']   
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists')
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            return redirect('signup')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            # user_login=auth.authenticate(username=username,password=password)
            # auth.login(request,user_login)
            # user_model=User.objects.get(username=username)
            signup_mod=Signup.objects.create(username=username,email=email)
            signup_mod.save()

            return redirect('login')
    else:
        return render(request,'signup.html')
@login_required(login_url='login')
def orders(request):
    return render(request,'orders.html')
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')