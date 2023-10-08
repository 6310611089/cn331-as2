from django.db import models
from courses.models import Course

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=100)
    registered_courses = models.ManyToManyField(Course, blank=True, related_name='student')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'