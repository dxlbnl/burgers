from django.contrib import admin

# Register your models here.
from client import models

class BurgerAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Burger, BurgerAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Order, OrderAdmin)



class IngredientTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.IngredientType, IngredientTypeAdmin)


class IngredientAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Ingredient, IngredientAdmin)

