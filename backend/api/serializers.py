"""Serializers for the API app."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для модели TASK."""

    class Meta:
        """Meta options for TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
