from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'students/home.html')
    return render(request, 'students/login.html')

def login(request):
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