from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('request_quota/<int:course_id>/', views.request_quota, name='request_quota'),
    path('cancel_request/<int:course_id>/', views.cancel_request, name='cancel_request'),
]