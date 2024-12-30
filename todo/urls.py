from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home), 
    path('contact/', contact), 
    path('todolist/', todo),
    path('todolist/createtask', createTask),
    path('todolist/<pk>', change_complete),
    path('todolist/<pk>/del_task/',delete_task),
    path('todolist/<pk>/edit_task/', edit_task)
    
]
