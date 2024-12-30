from django.db import models

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=50)
    description=models.TextField()
    state = models.BooleanField(default=False)