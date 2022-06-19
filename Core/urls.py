from django.urls import include, path
from Core import views

urlpatterns = [
    path('', views.home, name = 'home/'),
   
]