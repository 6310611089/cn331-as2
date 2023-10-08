from django.contrib import admin

# Register your models here.

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ['registered_courses']

admin.site.register(Student, StudentAdmin)