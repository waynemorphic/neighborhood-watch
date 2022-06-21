from django.shortcuts import render, redirect
from django.contrib.auth import logout
from Core.models import Resident, Neighborhood, Business, Post
from Core.forms import PostForm, ResidentForm, BusinessForm, NeighborhoodForm
from django.contrib.auth.models import User 
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

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

@login_required
def profile(request):
    current_user = request.user   
    try:            
        logged_user = Resident.objects.filter(name = current_user).first()        
        residents = Resident.objects.all()
        print(residents)
        form = ResidentForm()
        if request.method == 'POST':
            form = ResidentForm(request.POST)
            if form.is_valid():
                logged_user.name = form.save(commit = True)
                logged_user.id_number = form.cleaned_data['id_number']
                logged_user.neighborhood = form.cleaned_data['neighborhood']
                logged_user.email = form.cleaned_data['email']
                logged_user.save()
                
                messages.success(request, 'Profile set successfully')
                return redirect(to = 'user profile')
            print(User)
            print('hi')
        # resident_form = ResidentForm(instance = request.user.resident)
    except ObjectDoesNotExist:
        logged_in_user = User.objects.get(id = current_user.id)
        print(logged_in_user)
        
        resident_form = ResidentForm()
        if request.method == 'POST':
            resident_form = ResidentForm(request.POST)
            if resident_form.is_valid():
                resident = resident_form.save(commit = False)
                resident.user = logged_in_user
                print(resident)
                resident.save()
                
                messages.success(request, 'Profile set successfully')
                return redirect(to = 'user profile')                
                
        
    residents = Resident.objects.all()
    context = {"form": form, "residents": residents}
    return render(request, 'user/profile.html', context)

@login_required
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
            
            messages.success(request, 'Post added successfully') 
            return redirect(to = 'home/')          
    else:
        form = PostForm()       
    context = {"form": form} 
    return render (request, 'home/new_post.html', context)



def new_neighborhood(request):
    form = NeighborhoodForm()
    current_user = request.user
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST)
        logged_in_user = User.objects.get(username = current_user)
        if form.is_valid():
            logged_in_user = form.save(commit = True)
            logged_in_user.name = form.cleaned_data['name']
            logged_in_user.location = form.cleaned_data['location']
            logged_in_user.save()
            
            messages.success(request, 'Neighborhood added successfully') 
            return redirect(to = 'home/')          
    else:
        form = NeighborhoodForm()       
    context = {"form": form} 
    return render (request, 'home/new_hood.html', context)



def search_results(request):
    neighborhoods = Neighborhood.objects.all()
    if request.method == 'GET':
        name = request.GET.get('name')
        results = Neighborhood.objects.filter(name__contains=name).all()
        print(results)
        message = f'name'
        context = {
            'message': message, 
            'results': results
        }
        return render(request, 'home/search.html', context)
    else:
        messsage = 'No results found for the specified title'
        
    return render(request, 'home/search.html', {'messsage': messages})

def police(request):
    return render(request, 'utilities/police.html')

def health(request):
    return render(request, 'utilities/health.html')

def business(request):
    return render(request, 'utilities/businesses.html')

def sign_out(request):
    logout(request)
    
    return redirect( to = 'home/')