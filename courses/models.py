from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=60, unique=True)
    semester = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()
    course_open = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.course_id} ({self.course_name})'
    
class QuotaRequest(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quota_request')
    course_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.course}'