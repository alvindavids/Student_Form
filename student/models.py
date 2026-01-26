from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    degree = models.CharField(max_length=100)
    query = models.TextField()
