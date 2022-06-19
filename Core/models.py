from django.db import models
# from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User 

# Create your models here.
class Neighborhood(models.Model):
    '''
    Args:
        name, location, residents, admin
    '''
    name = models.CharField(max_length = 250, null = False)
    location = models.CharField(max_length = 250, null = False)
    residents = models.IntegerField(null = False)
    admin = models.ForeignKey(User, on_delete = models.CASCADE) 
    
    def __str__(self):
        return self.name
    

class Resident(models.Model):
    '''
    Args:
        name, id, neighborhood, email
    '''
    name = models.CharField(max_length = 250, null = False)
    id_number = models.IntegerField(null = False)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Business(models.Model):
    '''
    Args:
        name, user, neighborhood, email
    '''
    name = models.CharField(max_length = 250, null = False)
    user = models.ForeignKey(Resident, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField()
    
    def __str__(self):
        return self.name