from django.test import TestCase
from Core.models import Post, Business, Neighborhood, Resident
from django.contrib.auth.models import User

# Create your tests here.
class ResidentTestClass(TestCase):
    def setUp(self):
        self.new_user = User(email = 'one@gmail.com', username = 'John')
        self.new_user.save()
        
        self.new_neighborhood = Neighborhood(name = 'avenue', location = 'central', residents = '2000', admin = self.new_user)
        self.new_neighborhood.save()
        
        self.new_resident = Resident(name = 'doe', id_number = '123', neighborhood = self.new_neighborhood, email = '123@gmail.com')
        self.new_resident.save()
         
    def test_instance(self):
        self.assertTrue(self.new_resident, Resident)
        
    def test_save_resident(self):
        self.new_resident.save_resident()
        resident = Resident.objects.all()
        self.assertTrue(len (resident) > 0)
        
    def tearDown(self):
        Resident.objects.all().delete()
    
class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user = User(email = 'one@gmail.com', username = 'John')
        self.new_user.save()  
        
        self.new_neighborhood = Neighborhood(name = 'avenue', location = 'central', residents = '2000', admin = self.new_user)
        self.new_neighborhood.save()
        
        self.new_resident = Resident(name = 'doe', id_number = '123', neighborhood = self.new_neighborhood, email = '123@gmail.com')
        self.new_resident.save()
                                      
        self.new_business = Business(name = 'barbershop', user = self.new_resident, neighborhood = self.new_neighborhood, email = 'barbershop@gmail.com')
        self.new_business.save()
    
    def test_instance(self):
        self.assertTrue(self.new_business, Business)
    
    def test_save_business(self):
        self.new_business.save_business()
        business = Business.objects.all()
        self.assertTrue(len (business) > 0)
        
    def tearDown(self):
        Business.objects.all().delete()
        
class NeighborhoodTestClass(TestCase):
    def setUp(self):         
        self.new_user = User(email = 'one@gmail.com', username = 'John')
        self.new_user.save()         
        
        self.new_neighborhood = Neighborhood(name = 'avenue', location = 'central', residents = '2000', admin = self.new_user)
        self.new_neighborhood.save()
        
    def test_instance(self):
        self.assertTrue(self.new_neighborhood, Neighborhood)
        
    def test_save_neighborhood(self):
        self.new_neighborhood.save_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len (neighborhood) > 0)
        
    def tearDown(self):
        Neighborhood.objects.all().delete()
        
class PostTestClass(TestCase):
    def setUp(self):                
        self.new_user = User(email = 'one@gmail.com', username = 'John')
        self.new_user.save()
        
        self.new_neighborhood = Neighborhood(name = 'avenue', location = 'central', residents = '2000', admin = self.new_user)
        self.new_neighborhood.save()
         
        self.new_post = Post(username = self.new_user, post = 'nice place', neighborhood = self.new_neighborhood)
        self.new_post.save()
        
    def test_instance(self):
        self.assertTrue(self.new_post, Post)
        
    def tearDown(self):
        Post.objects.all().delete()