from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'due_date', 'is_important', 'is_completed')
    list_filter = ('category', 'is_important', 'is_completed')
    search_fields = ('title', 'description')
    date_hierarchy = 'due_date'