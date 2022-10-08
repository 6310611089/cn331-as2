from django.contrib import admin
from .models import Subject, Enrollment

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("sub_id", "sub_name", "semester", "year", "seat", "status")

class EnrollmentAdmin(admin.ModelAdmin):
    filter_horizontal = ("sub_enroll",)

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)