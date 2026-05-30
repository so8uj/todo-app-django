from django.shortcuts import render

from todo.models import Todo

def index(request):

    completed_todos = Todo.objects.filter(completed=True)
    pending_todos = Todo.objects.filter(completed=False)

    context = {
        'completed_todos': completed_todos,
        'pending_todos': pending_todos,
    }

    return render(request, 'index.html', context)