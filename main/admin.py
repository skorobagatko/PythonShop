from django.contrib import admin
from main.models import *
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
