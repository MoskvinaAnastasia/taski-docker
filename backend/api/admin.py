"""Admin configuration for the Task model."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Представление администратора для модели задач."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
