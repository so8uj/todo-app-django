from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Todo

# Create your views here.
def addTodo(request):

    title = request.POST.get('title')
    description = request.POST.get('description')

    Todo.objects.create(
        title=title,
        description=description,
    )    

    return redirect('index')



def changeStatus(request,todo_status,todo_id):

    todo = Todo.objects.get(id=todo_id)
    todo.completed = True if todo_status == 1 else False
    todo.save()

    return redirect('index')


def updateTodo(request,todo_id):

    title = request.POST.get('title')
    description = request.POST.get('description')

    todo = Todo.objects.get(id=todo_id)
    todo.title = title
    todo.description = description
    todo.save()

    return redirect('index')