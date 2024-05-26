from django.contrib import admin
from .models import Client, Product, Order


# Register your models here.


class ClientFilter(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'registration_date',)
    list_filter = ('name',)
    search_fields = ('name',)


class ProductFilter(admin.ModelAdmin):
    list_display = ('name',
                    'description',
                    'price',
                    'quantity',
                    'added_date',
                    'photo',)
    list_filter = ('name', 'price')
    search_fields = ('name',)


class OrderFilter(admin.ModelAdmin):
    list_display = ('client',
                    'total_amount',
                    'order_date',)
    list_filter = ('client',)
    search_fields = ('client',)


admin.site.register(Client, ClientFilter)
admin.site.register(Product, ProductFilter)
admin.site.register(Order, OrderFilter)
