from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Department(models.Model):
        dept_name = models.CharField(max_length=100)
        dept_code = models.CharField(max_length=10)

        def __str__(self):
             return self.dept_code

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    department = models.ForeignKey(
        Department,
        on_delete = models.CASCADE,#if Author is deleted works will also delete
        related_name='students'
    )

    class Meta():
        ordering = ['name']

    def __str__(self):
        return self.name
    

    