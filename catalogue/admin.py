from django.contrib import admin
from .models import Cheese, Review, Customer, UserProfile

# Register your models here.
admin.site.register(Cheese)
admin.site.register(Review)
admin.site.register(Customer)
admin.site.register(UserProfile)