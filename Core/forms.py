from django import forms
from django.conf import UserSettingsHolder
from Core.models import Resident, Business, Neighborhood, Post
from django.contrib.auth.models import User 

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ['name', 'id_number', 'email', 'neighborhood']
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'user', 'neighborhood', 'email']        
        
class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['name', 'location', 'residents']
        exclude = ['admin']                
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post','username', 'neighborhood']
        # exclude = []

