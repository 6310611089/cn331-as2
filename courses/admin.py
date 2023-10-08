from django.contrib import admin

# Register your models here.

from .models import Course, CourseInfo

class CourseInfoAdmin(admin.ModelAdmin):
    list_display = ['course', 'semester', 'year', 'seat', 'course_status']

admin.site.register(Course)
admin.site.register(CourseInfo, CourseInfoAdmin)