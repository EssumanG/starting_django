from django.db import models
from django.utils import timezone


# Create your models here.

class TaskModel(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    
    
    class Meta:
        """Meta definition for  Task."""

        verbose_name = ' Task'
        verbose_name_plural = ' Tasks'

    def __str__(self):
        """Unicode representation of  Task."""
        pass