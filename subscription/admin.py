from django.contrib import admin

from subscription.models import RegisteredCourse, RegisteredExam
from subscription.models import RegisteredExam

# Register your models here.
class RegisteredCourseAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'email','amount', "date_created"]
    search_fields = ['user', 'email']

admin.site.register(RegisteredCourse, RegisteredCourseAdmin)

admin.site.register(RegisteredExam)
