from django.shortcuts import render,HttpResponse,redirect
from todo.models import Todolist

# Create your views here.
def home(request):
    person =[
        {"name":"Nisha","age":23},
        {"name":"isha","age":53},
        {"name":"miha","age":13},
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 22},
        {"name": "Diana", "age": 28},
        {"name": "Ethan", "age": 35},
        {"name": "Fiona", "age": 26},
        {"name": "George", "age": 29},
        {"name": "Hannah", "age": 24},
        {"name": "Ian", "age": 31},
        {"name": "Julia", "age": 27}
    ]
    context = {
        "key":"Anisha",
        "p":person
    }
    return render(request,'index.html',context) 
    # return HttpResponse("First app")

def contact(request):
    return render(request,'contact.html')



def todo(request):
    tasks = Todolist.objects.all() #Todolist class is obtained from models.py 
    total_tasks = tasks.count() #cout the number of task
    pending_tasks =tasks.filter(state=False).count()
    complete_tasks= tasks.filter(state=True).count()
    context = {
        "t" : tasks,
        "total_task" : total_tasks,
        "pend_task" : pending_tasks,
        "comp_task" : complete_tasks
    }
    return render(request,'todolist.html',context)

def createTask(request):
    if request.method == "POST": #if request gareko method post (from create.html) vayo vane---
        titles = request.POST.get('title')
        descriptions = request.POST.get('description')
        if titles == "" and descriptions == "":
            context = {
                "error": "Both field are empty"
            }
            return render(request,'create.html',context)  
        Todolist.objects.create(title = titles, description = descriptions)  
        return redirect('/todolist') 
        # return  HttpResponse(descriptions)
       
    return render(request,'create.html')

def change_complete(request,pk):
    tasks = Todolist.objects.get(pk = pk)
    tasks.state = True
    tasks.save()
    return redirect('/todolist')

def delete_task(request,pk):
    tasks = Todolist.objects.get(pk = pk)
    tasks.delete()
    return redirect('/todolist')
    
    

def edit_task(request,pk):
    #Retrieve the task object 
    tasks = Todolist.objects.get(pk = pk)
    if request.method=='POST':
        # Get the title and description from the POST data
        titles = request.POST.get('title').strip()
        descriptions = request.POST.get('description').strip()
        
        # Check if both fields are empty
        if titles =="" and descriptions =="":
            context = {
                "error_msg":"both field are empty",
                "edit_task_key": tasks
                }
            return render(request,'edit_task.html',context)
        
        # Update the task object
        tasks.title=titles
        tasks.description=descriptions
        tasks.save()
        
        return redirect('/todolist')
    context ={
        "edit_task_key": tasks
    }
    return render(request,'edit_task.html',context)
    