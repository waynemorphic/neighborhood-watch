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
    admin = models.ForeignKey(User, on_delete = models.CASCADE, null = True) 
    
    def __str__(self):
        return self.name
    
    def save_neighborhood(self):
        self.save() 
    
    def delete_neighborhood(self):
        self.objects.all().delete()
    
    def create_neighborhood(self):
        new_neighborhood = Neighborhood(name = self.name, location = self.location, residents = self.residents)
        new_neighborhood.save()
        return new_neighborhood
    
    def update_neighborhood(self):
        update_neighborhood = Neighborhood.objects.filter(id = id).update(name = self.name, location = self.location)
        return update_neighborhood
    
    def update_occupants(self):
        update_occupants = Neighborhood.objects.filter(id = self.residents.id).update(residents = self.residents)
        return update_occupants
    
    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        findings = cls.objects.filter(name__icontains = neighborhood_id)
        return findings
        
class Resident(models.Model):
    '''
    Args:
        name, id_number, neighborhood, email
    '''
    name = models.CharField(max_length = 250, null = False)
    id_number = models.IntegerField(null = False)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
    def save_resident(self):
        self.save() 

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
    
    def save_business(self):
        self.save() 
    
    def delete_business(self):
        self.objects.all().delete()
    
    def create_business(self):
        new_business = Business(name = self.name, user = self.user, neighborhood = self.neighborhood)
        new_business.save()
        return new_business
    
    def update_business(self):
        update_business = Business.objects.filter(id = id).update(name = self.name, email = self.email, neighborhood = self.neighborhood)
        return update_business
    
    @classmethod
    def find_business(cls, business_id):
        findings = cls.objects.filter(name__icontains = business_id)
        return findings
    
class Post(models.Model):
    '''
    Args:
        username, post, neighborhood
    '''
    username = models.ForeignKey(User, on_delete=models.CASCADE, null= False)
    post = models.TextField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null= False)