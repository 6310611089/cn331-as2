from django.db import models

# Create your models here.

class Subject(models.Model):
    subID = models.CharField(max_length=10, primary_key=True)
    subName = models.CharField(max_length=100)
    semester = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.subID} ({self.subName})"

class Student(models.Model):
    sID = models.IntegerField()
    sName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sName}"

class Apply(models.Model):
    subID = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subjectID")
    sApply = models.CharField(max_length=10) 

    def __str__(self):
        return f"{self.subID}: {self.sApply}"
    