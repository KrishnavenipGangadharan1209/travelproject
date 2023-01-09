from django.shortcuts import render
from . models import *
from django.http import HttpRequest

# Create your views here.
def index(request):

    obj=Place.objects.all()
    obj1=Teammates.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})


