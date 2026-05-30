from django.shortcuts import redirect, render

from todo.models import Todo

def index(request):

    completed_todos = Todo.objects.filter(completed=True)
    pending_todos = Todo.objects.filter(completed=False)

    action = request.GET.get('action') or 'add'
    todo_id = request.GET.get('id')

    
    

    todo = None
    if not todo_id:
        action = 'add'
    if todo_id and action != 'add':
        todo = Todo.objects.filter(id=todo_id).first()
        if not todo:
            return redirect('index')
    

    context = {
        'completed_todos': completed_todos,
        'pending_todos': pending_todos,
        'action': action,
        'todo': todo,
    }

    return render(request, 'index.html', context)