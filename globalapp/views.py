from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth import authenticate,login,logout
from globalapp.form.account import RegistrationForm

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



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('home')
        else:
            # If invalid, stay on the same page and show errors
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})


# def register(request):
#   print(request.POST['name'])

#   get_mode = Account.objects.create({
#     name:request.POST['name'],
#     passwod:request.POST['password']
#   })
#   return request.POST
# Create your views here.
