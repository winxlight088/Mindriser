from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id',"category_name"]
    search_fields = ['category_name']

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id','food_name', 'food_price', 'category_id']
    search_fields = ['food_name', 'food_price']
    autocomplete_fields = ['category']
    # list_filter = ['food_price']
    

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['id','table_number', 'is_available']
    list_filter = ['is_available']
    list_editable = ['is_available']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    autocomplete_fields = ['food']
    # extra
 
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','order_status','total_price','payment_status','table']
    list_filter = ['order_status','payment_status']
    list_editable = ['order_status','payment_status']
    inlines = [OrderItemInline]
    
    

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     # list_filter = []
#     # search_fields = ['food_id']
#     list_display = ['id', 'order_id', 'food_id']
