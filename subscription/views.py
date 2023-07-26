from django.shortcuts import render, redirect, reverse, get_object_or_404
from acetelapp.models import Course, Exam
import json
import requests
from django.conf import settings
from .models import RegisteredCourse


def payment_init(request, course_id):
    
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        email = request.POST.get('email')
        amount = request.POST.get('amount')

        registered_course = RegisteredCourse.objects.create(email=email, amount=amount, course=course, user=request.user)
        registered_course.save()

        return render(request, 'subscription/success.html', {'course': course})
    

    return render(request,'subscription/payment.html', {'course': course})


def exam_payment_init(request, exam_id):
    
    exam = get_object_or_404(Exam, pk=exam_id)

    if request.method == 'POST':
        email = request.POST.get('email')
        amount = request.POST.get('amount')

        registered_exam = RegisteredExam.objects.create(email=email, amount=amount, exam=exam, user=request.user)
        registered_exam.save()

        return render(request, 'subscription/success.html', {'exam': exam})
    

    return render(request,'subscription/exam_payment.html', {'exam': exam})


api_key = settings.PAYSTACK_SECRET_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL

def processpayment(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    if request.method == 'POST':
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        
        
        success_url = request.build_absolute_uri(reverse('subscription:payment_init',  kwargs={'course_id':course_id}))
        cancel_url = request.build_absolute_uri(reverse('subscription:canceled'))
    
        metadata = json.dumps({"course_id":course_id, "cancel_action": cancel_url})
       
        # Paystack checkout session data
        api_key = settings.PAYSTACK_SECRET_KEY
        session_data = {'email': email, 'amount': int(float(amount))*100, 'callback_url': success_url, 'metadata': metadata}
        headers = {"authorization": f"Bearer {api_key}"}
        
        # API request to Paystack server
        
        r = requests.post(url, headers=headers, json=session_data)
        response = r.json()
    
        if response.get("status"):
            # Redirect to Paystack payment form
            redirect_url = response["data"]["authorization_url"]
            
            return redirect(redirect_url, code=303)
        else:
            return render(request, 'subscription/payment.html', {'course': course, 'error': response.get("message")})

    return render(request, 'subscrition/payment.html', {'course': course})


def exam_processpayment(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    
    if request.method == 'POST':
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        
        success_url = request.build_absolute_uri(reverse('subscription:exam_payment_init', kwargs={'exam_id':exam_id}))
        cancel_url = request.build_absolute_uri(reverse('subscription:canceled'))
    
        metadata = json.dumps({"exam_id":exam_id, "cancel_action": cancel_url})
       
        # Paystack checkout session data
        api_key = settings.PAYSTACK_SECRET_KEY
        session_data = {'email': email, 'amount': int(float(amount)) * 100, 'callback_url': success_url, 'metadata': metadata}
        headers = {"authorization": f"Bearer {api_key}"}
        
        # API request to Paystack server
        url = 'https://api.paystack.co/checkout/initialize'
        r = requests.post(url, headers=headers, json=session_data)
        response = r.json()
    
        if response.get("status"):
            # Redirect to Paystack payment form
            redirect_url = response["data"]["authorization_url"]
            return redirect(redirect_url, code=303)
        else:
            return render(request, 'subscription/exam_payment.html', {'exam':exam, 'error': response.get("message")})

    return render(request, 'subscription/exam_payment.html', {'exam':exam})



def payment_canceled(request):
 return render(request, 'subscription/canceled.html')