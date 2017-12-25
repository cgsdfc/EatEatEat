from django.contrib import admin
from .models import Dish, Restaurant, DishInstance, ResInstance

admin.site.register(Dish)
admin.site.register(Restaurant)
admin.site.register(DishInstance)
admin.site.register(ResInstance)

# Register your models here.
