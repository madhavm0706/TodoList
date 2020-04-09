from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todo_list' : todos
    }
    return render(request,'Todo/todo_list.html',context)

def todo_details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }    
    return render(request,'Todo/todo_details.html',context)

def todo_create(request):
    form = TodoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'Todo/todo_create.html',context)   


def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)  
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form':form}
    return render(request,'Todo/todo_update.html',context)       

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/")