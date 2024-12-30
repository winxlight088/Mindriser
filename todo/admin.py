from django.contrib import admin
from todo.models import *

# Register your models here.
class TodolistAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','state'] #list_display  is predefined variable
    list_filter= ['state']
    list_per_page = 5
    search_fields = ['title']
    
admin.site.register(Todolist,TodolistAdmin)