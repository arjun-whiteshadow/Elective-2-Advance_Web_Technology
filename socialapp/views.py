from cgitb import html
from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

# Create your views here.

def login(request):
   return render(request,'socialapp/login.html')
