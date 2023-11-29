from django.contrib import admin
from order.models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'drink', 'ice', 'suger',
                    'add', 'price', 'amount', 'uid', 'is_checkout')


admin.site.register(Order, OrderAdmin)
