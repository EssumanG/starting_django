from rest_framework import serializers
from .models import TaskModel



class TaskModelSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=60)
    class Meta:
        model = TaskModel
        fields = ["id", "title", "description", "date_created","deadline","is_done"]
            
        