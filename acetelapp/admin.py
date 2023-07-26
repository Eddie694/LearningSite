from django.contrib import admin
from . models import Course, Exam

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display =['title', 'amount', 'date']
    search_fields = ['title', 'description']
   
admin.site.register(Course, CourseAdmin)


class ExamAdmin(admin.ModelAdmin):
    list_display =['title', 'amount']
    search_fields = ['title', 'description']

admin.site.register(Exam, ExamAdmin)


