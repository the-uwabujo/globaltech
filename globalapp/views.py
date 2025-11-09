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

def user_dashboard(request):
    return render(request, 'user-dashboard.html')


def admin_dashboard(request):
    return render(request, 'Admin/admin-dashboard.html')




def register(request):
    print(request.POST)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.errors)
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


def login_view(request):
    """
    Login with email and password.
    Expects POST with 'email' and 'password'. Renders 'login.html' on GET or on failure.
    Redirects to 'home' on success.
    """
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        print(request.POST)
        # Try standard authenticate (username=email) and then a fallback using 'email' kwarg
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('admin-dashboard')
            else:
              return redirect('user-dashboard')
        # Authentication failed
        return render(request, 'login.html', {'error': 'Invalid email or password', 'email': email})
    return render(request, 'login.html')
