from django.contrib import admin

from todo.models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    list_filter = ('completed',)
    search_fields = ('title', 'description')

admin.site.register(Todo, TodoAdmin)