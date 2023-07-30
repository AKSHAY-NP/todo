from django.db import models

# Create your models here.
class TaskModel(models.Model):
    task=models.CharField( max_length=50)
    priority=models.IntegerField(default=0)
    date=models.DateField()