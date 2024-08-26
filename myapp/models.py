from django.db import models

# Create your models here.
#Create classes
class Project(models.Model):
    #CharField is used to define short to medium length strings
    name = models.CharField(max_length=200)
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    