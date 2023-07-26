from django.urls import path
from . import views

app_name ='acetelapp'

urlpatterns = [
   path('', views.index, name='index'),
   path('courses/', views.courses, name='courses'),
   path('exams/', views.exams, name='exams'),
   path('login_courses/', views.login_courses, name='login_courses'),
   path('login_exams/', views.login_exams, name='login_exams'),
   path('login_page/', views.login_page, name='login_page'),
   path('mycourse/', views.mycourse, name='mycourse'),
   path('myexams/', views.myexams, name='myexams'),
   path('registercourse/<int:course_id>/', views.registercourse, name ='registercourse'),
   path('registerexam/<int:exam_id>/', views.registerexam, name ='registerexam')
]