from django.contrib import admin

# Register your models here.
from client.models import Order, Burger

class BurgerAdmin(admin.ModelAdmin):
    pass
class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Burger, BurgerAdmin)
admin.site.register(Order, OrderAdmin)