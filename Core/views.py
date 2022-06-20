from re import T
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from Core.models import Resident, Neighborhood, Business, Post
from Core.forms import PostForm, ResidentForm, BusinessForm, NeighborhoodForm
from django.contrib.auth.models import User 
from django.contrib import messages

# Create your views here.
def home(request):   
    posts = Post.objects.all()
    neighborhoods = Neighborhood.objects.all()
    form = NeighborhoodForm()    
    current_user = request.user
    
    # new user has to be attached to their specific neighborhood
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST)
        logged_user = User.objects.get(username = current_user)
        if form.is_valid():
            name = form.save(commit=True)
            logged_user.name = form.cleaned_data['name']
            logged_user.location = form.cleaned_data['location']
            logged_user.residents = form.cleaned_data['residents']
            logged_user.save()
            
            messages.success(request,'Your neighborhood has been added successfully')
            return redirect(to = 'home/')
                
    context = {"posts": posts, "form": form}
    return render(request, 'home/home.html', context)

def profile(request):
    current_user = request.user
    logged_user = User.objects.get(username = current_user)
    form = ResidentForm()
    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if form.is_valid():
            logged_user.name = form.save(commit = True)
            logged_user.id_number = form.cleaned_data['id_number']
            logged_user.neighborhood = form.cleaned_data['neighborhood']
            logged_user.email = form.cleaned_data['email']
            logged_user.save()
            
            messages.success(request, 'Profile updated successfully')
            return redirect(to = 'user profile')
        else:
            form = ResidentForm()
    context = {"form": form}
    return render(request, 'user/profile.html', context)

def new_post(request):
    form = PostForm()
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        logged_in_user = User.objects.get(username = current_user)
        if form.is_valid():
            logged_in_user = form.save(commit = True)
            logged_in_user.username = form.cleaned_data['username']
            logged_in_user.neighborhood = form.cleaned_data['neighborhood']
            logged_in_user.post = form.cleaned_data['post']
            logged_in_user.save()
            
            messages.success = 'Post added successfully'
            return redirect(to = 'home/')          
    else:
        form = PostForm()       
    context = {"form": form} 
    return render (request, 'home/new_post.html', context)

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