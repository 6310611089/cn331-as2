from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Course, QuotaRequest
# Create your views here.

def register(request):
    search_query = request.GET.get('search', '')

    courses = Course.objects.filter(course_name__icontains=search_query) | Course.objects.filter(course_id__icontains=search_query)

    context = { 'courses': courses }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'courses/register.html', context)
    

def request_quota(request, course_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login') 

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return redirect('register') 

        if course.seat <= 0:
            return redirect('register')  

        existing_request = QuotaRequest.objects.filter(student=request.user, course=course).exists()
        if existing_request:
            return redirect('register') 

        quota_request = QuotaRequest(student=request.user, course=course, course_approved=False)
        quota_request.save()

        course.seat -= 1
        course.save()

        return redirect('register')  

    return redirect('register')


def cancel_request(request, course_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    course = Course.objects.get(id=course_id)

    quota_request = QuotaRequest.objects.filter(student=request.user, course=course).first()
    quota_request.delete()

    course.seat += 1
    course.save()

    return redirect('home')