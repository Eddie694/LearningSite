from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from subscription.models import RegisteredCourse, RegisteredExam
from . models import Course, Exam
from accounts.models import User
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta



# Create your views here.
def index(request):
    exams = Exam.objects.all()
    #Get couses according to number of subscribers
    courses = Course.objects.annotate(num_users_registered=Count('registeredcourse'))
 
    for course in courses:
        duration = timezone.now() - course.date
        minutes = duration.total_seconds() / 60

        if minutes < 1:
            course.date= "Just Now"
        elif minutes < 60:
            course.date= f"{int(minutes)} minutes ago"
        elif minutes < 1440: 
            course.date =f"{int(minutes // 60)} hours ago"
        else:
            days = duration.days
            if days == 1:
                course.date="1 day ago"
            else:
                course.date =f"{days} days ago"
    
    context = {
        'courses': courses,
        'exams': exams,
                    
    }

    return render(request, 'acetelapp/index.html', context)

   
    
def courses(request):
    #Get couses according to number of subscribers
    courses = Course.objects.annotate(num_users_registered=Count('registeredcourse'))
    for course in courses:
        duration = timezone.now() - course.date
        minutes = duration.total_seconds() / 60

        if minutes < 1:
            course.date= "Just Now"
        elif minutes < 60:
            course.date= f"{int(minutes)} minutes ago"
        elif minutes < 1440: 
            course.date =f"{int(minutes // 60)} hours ago"
        else:
            days = duration.days
            if days == 1:
                course.date="1 day ago"
            else:
                course.date =f"{days} days ago"
    
    context = {
        'courses': courses,
        'exams': exams,
            
    }
    context = {
        'courses':courses
    }
    return render(request, 'acetelapp/courses.html', context)

def exams(request):
    exams = Exam.objects.all()
    context = {
        'exams': exams
    }
    return render(request, 'acetelapp/exams.html', context)


def login_page(request):
    #Get couses according to number of subscribers
    courses = Course.objects.annotate(num_users_registered=Count('registeredcourse'))
    exams = Exam.objects.all()
    if request.user.is_authenticated:
        user = request.user
        login(request, user)
        first_name = user.first_name
        user_first_letter = user.first_name[0]
    else:
        return redirect('accounts:login')
    
    for course in courses:
        duration = timezone.now() - course.date
        minutes = duration.total_seconds() / 60

        if minutes < 1:
            course.date= "Just Now"
        elif minutes < 60:
            course.date= f"{int(minutes)} minutes ago"
        elif minutes < 1440: 
            course.date =f"{int(minutes // 60)} hours ago"
        else:
            days = duration.days
            if days == 1:
                course.date="1 day ago"
            else:
                course.date =f"{days} days ago"

    context = {
        'first_name': first_name,
        'user_first_letter': user_first_letter,
        'courses': courses,
        'exams': exams,
    }
    return render(request, 'acetelapp/login_page.html', context)

def login_courses(request):
    #Get couses according to number of subscribers
    courses = Course.objects.annotate(num_users_registered=Count('registeredcourse'))
       
    if request.user.is_authenticated:
        user = request.user
        login(request, user)
        first_name = user.first_name
        user_first_letter = user.first_name[0]
    else:
        return redirect('accounts:login')

    for course in courses:
        duration = timezone.now() - course.date
        minutes = duration.total_seconds() / 60

        if minutes < 1:
            course.date= "Just Now"
        elif minutes < 60:
            course.date= f"{int(minutes)} minutes ago"
        elif minutes < 1440: 
            course.date =f"{int(minutes // 60)} hours ago"
        else:
            days = duration.days
            if days == 1:
                course.date="1 day ago"
            else:
                course.date =f"{days} days ago"
    
    context = {
        'first_name': first_name,
        'user_first_letter': user_first_letter,
        'courses': courses,
        'exams': exams,
    }

    return render(request, 'acetelapp/login_courses.html', context)

def login_exams(request):
    exams = Exam.objects.all()
    if request.user.is_authenticated:
        user = request.user
        login(request, user)
        first_name = user.first_name
        user_first_letter = user.first_name[0]
    else:
        return redirect('accounts:login')

    context = {
        'first_name': first_name,
        'user_first_letter': user_first_letter,
        'courses': courses,
        'exams': exams,
    }

    return render(request, 'acetelapp/login_exams.html', context)

def mycourse(request):
    user = request.user
    # Fetch the registered courses for the current user
    registered_courses = RegisteredCourse.objects.filter(user=user)
    #Get couses according to number of subscribers
    registered_courses = registered_courses.annotate(num_users=Count('course__registeredcourse'))
    
    if request.user.is_authenticated:
        user = request.user
        login(request, user)
        first_name = user.first_name
        user_first_letter = user.first_name[0]
    else:
        return redirect('accounts:login')

    for registered_course in registered_courses:
        duration = timezone.now() - registered_course.course.date
        minutes = duration.total_seconds() / 60

        if minutes < 1:
            registered_course.course.date= "Just Now"
        elif minutes < 60:
            registered_course.course.date= f"{int(minutes)} minutes ago"
        elif minutes < 1440: 
            registered_course.course.date =f"{int(minutes // 60)} hours ago"
        else:
            days = duration.days
            if days == 1:
                registered_course.course.date="1 day ago"
            else:
                registered_course.course.date =f"{days} days ago"

    context = {
        'courses':courses,
        'first_name': first_name,
        'user_first_letter': user_first_letter,
        'registered_courses': registered_courses,
        'registered_courses': registered_courses,
    }

    return render(request, 'acetelapp/mycourse.html', context)

def myexams(request):
    registered_exams=RegisteredExam.objects.all()
    if request.user.is_authenticated:
        user = request.user
        login(request, user)
        first_name = user.first_name
        user_first_letter = user.first_name[0]
    else:
        return redirect('accounts:login')

    context = {
        'first_name': first_name,
        'user_first_letter': user_first_letter,
        'registered_exams':registered_exams,
    }
   
    return render(request, 'acetelapp/myexams.html', context)


def registercourse(request, course_id):
    course = get_object_or_404(Course, id = course_id)
    if request.user.is_authenticated:
        user = request.user
        login(request, user)
        first_name = user.first_name
        user_first_letter = user.first_name[0]
    else:
        return redirect('accounts:login')
    context ={
        'course' : course,
        'first_name' : first_name,
        'user_first_letter':user_first_letter,
    }
    return render (request,'acetelapp/registercourse.html', context )



def registerexam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if request.user.is_authenticated:
        user = request.user
        login(request, user)
        first_name = user.first_name
        user_first_letter = user.first_name[0]
    else:
        return redirect('accounts:login')
    context ={
        'exam' : exam,
        'first_name' : first_name,
        'user_first_letter':user_first_letter,
        }
    return render (request,'acetelapp/registerexam.html', context  )

