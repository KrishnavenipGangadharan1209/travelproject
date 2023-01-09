from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import *
from django.http import HttpRequest

# Create your views here.

def login(request):

    if request.method=='POST':
        usernamr=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=usernamr,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid info')
            return redirect('login')

    return render(request,'login.html')


def register(request):

    if request.method== 'POST':
        username = request.POST['user_name']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        pass1 = request.POST['user_password']
        pass2 = request.POST['confirm_password']
        email = request.POST['email']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:

                user=User.objects.create_user(username=username,first_name=fname,last_name=lname,password=pass1,email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password are not same')
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')

def logout(request):

    auth.logout(request)
    return redirect('/')