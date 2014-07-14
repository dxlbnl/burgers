from django.contrib import admin

# Register your models here.
from client import models







class BurgerContentInline(admin.StackedInline):
	model = models.BurgerContents
	readonly_fields = ('ingredient',)

class BurgerAdmin(admin.ModelAdmin):
	inlines = [
		BurgerContentInline
	]

class OrderAdmin(admin.ModelAdmin):
    pass


class IngredientAdmin(admin.ModelAdmin):
	pass
    
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Burger, BurgerAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)

