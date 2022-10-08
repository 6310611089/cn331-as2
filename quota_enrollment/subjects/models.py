from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    sub_id = models.CharField(max_length=10, primary_key=True)
    sub_name = models.CharField(max_length=64)
    semester = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.sub_id} ({self.sub_name})"

    def is_seat_available(self):
        return self.students.count() < self.seat

class Enrollment(models.Model):
    student_name = models.ForeignKey(User, on_delete=models.CASCADE)
    sub_enroll = models.ManyToManyField(Subject, blank=True, related_name="students")
    