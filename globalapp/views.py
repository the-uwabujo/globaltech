from django.shortcuts import render
from django.http import request

def home(request):
  return render (request, 'home.html')

def about_us(request):
  return render (request, 'about-us.html')

def secure_your_device(request):
  return render (request, 'secure-your-device.html')

def contact_us(request):
  return render (request, 'contact-us.html')

def select_lang(request):
  return render (request, 'select-lang.html')

def verify(request):
  return render (request, 'verify.html')

def login(request):
  return render (request, 'login.html')

# Create your views here.
