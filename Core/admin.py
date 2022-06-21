from django.contrib import admin
from Core.models import Post, Business, Resident, Neighborhood

# Register your models here.
admin.site.register(Business)
admin.site.register(Resident)
admin.site.register(Post)
admin.site.register(Neighborhood)