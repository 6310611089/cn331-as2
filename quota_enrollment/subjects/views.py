from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Subject

# Create your views here.
def index(request):
    return render(request, "subjects/index.html", {
        "subjects": Subject.objects.all()
    })

def enroll(request, subject_id):
    if request.method == "POST":
        subject = get_object_or_404(Subject, pk=subject_id)
        student = get_object_or_404(User, pk=subject_id)
        if student not in subject.students.all() and course.is_seat_available():
            student = Student.objects.get(pk=int(request.POST["student"]))
            student.register.add(course)
    return HttpResponseRedirect(reverse("register:course"), args=(subject_id,))