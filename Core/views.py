from django.shortcuts import render
from django.contrib.auth import logout, login

# Create your views here.
def sign_out(request):
    logout(request)
    return render(request, 'home/index.html')