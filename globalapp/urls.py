from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('about-us/',views.about_us, name = 'about-us'),
    path('secure-your-device/',views.secure_your_device, name = 'secure-your-device'),
    path('contact-us/',views.contact_us, name = 'contact-us'),
    path('select-lang/',views.select_lang, name = 'select-lang'),
    path('verify/',views.verify, name = 'verify'),
    #path('login/',views.login, name = 'login'),
    path('register/',views.register, name = 'register'),

]