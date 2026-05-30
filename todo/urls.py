from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.addTodo, name='addTodo'),
    path('status/<int:todo_status>/<int:todo_id>/',views.changeStatus, name='changeStatus'),
    path('update/<int:todo_id>/',views.updateTodo, name='updateTodo'),
]