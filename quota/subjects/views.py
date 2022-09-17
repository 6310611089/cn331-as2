from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Subject
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def course(request):
    courses = Subject.objects.all()
    context = { 'course': courses }
    return render(request, 'subjects/course.html', context)

@login_required
def apply(request):
    return render(request, 'subjects/apply.html')