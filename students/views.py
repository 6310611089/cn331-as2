from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from courses.models import Course, QuotaRequest

# Create your views here.

def home(request):
    if request.user.is_staff:
        return HttpResponseRedirect(reverse('admin:index'))
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    user_courses = QuotaRequest.objects.filter(student=request.user)

    context = {'user_courses': user_courses}

    return render(request, 'students/home.html', context)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'students/login.html', {
                'message': 'Invalid credentials.'
            })
    return render(request, 'students/login.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))