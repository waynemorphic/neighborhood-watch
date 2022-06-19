from django.shortcuts import render
from django.contrib.auth import logout, login

# Create your views here.
def home(request):    
    return render(request, 'home/home.html')

def profile(request):
    return render(request, 'user/profile.html')

def new_post(request):
    return render (request, 'home/new_post.html')

def search_results(request):
    return render(request, 'home/search.html')

def police(request):
    return render(request, 'utilities/police.html')

def health(request):
    return render(request, 'utilities/health.html')

def business(request):
    return render(request, 'utilities/businesses.html')

def sign_out(request):
    logout(request)
    return render(request, 'home/home.html')