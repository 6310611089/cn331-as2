from django.contrib import admin
from .models import Course, QuotaRequest

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'semester', 'year', 'seat', 'course_open')
    list_filter = ('semester', 'year', 'course_open')
    search_fields = ('course_id', 'course_name', 'semester', 'year')
    list_editable = ('seat', 'course_open')

class QuotaRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'course_approved')

admin.site.register(Course, CourseAdmin)
admin.site.register(QuotaRequest, QuotaRequestAdmin)