from django.contrib import admin

from .models import Subject, Student, Apply

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("subID", "subName")

class StudentAdmin(admin.ModelAdmin):
    list_display = ("sID", "sName")

class ApplyAdmin(admin.ModelAdmin):
    list_display = ("subID", "sApply")


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Apply, ApplyAdmin)