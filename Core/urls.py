from django.urls import include, path
from Core import views

urlpatterns = [
    path('', views.home, name = 'home/'),
    path('home/new_post', views.new_post, name = 'add post'),
    path('home/profile', views.profile, name = 'user profile'),
    path('home/police', views.police, name = 'police'),
    path('home/businesses', views.business, name = 'business'),
    path('home/health_services', views.health, name = 'health'),
    path('home/search_results', views.search_results, name = 'search results'),
    path('logout', views.sign_out, name = 'logout'),
   
]