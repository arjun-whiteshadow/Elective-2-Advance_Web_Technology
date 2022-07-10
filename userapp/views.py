from django.shortcuts import render,HttpResponse
from django.template import loader
from cgitb import html
# Create your views here.

def login(request):
   return render(request,'userapp/login.html')



def blank(request):
    return render(request,'userapp/blank.html')

def doLogin(request):
     return render(request,'userapp/home.html')
