from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Spot, Dish, DishModifier, Category

admin.site.register(DishModifier, MPTTModelAdmin)

admin.site.register(Spot)
admin.site.register(Dish)
admin.site.register(Category)
