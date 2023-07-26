from django.urls import path
from . import views

app_name = 'subscription'

urlpatterns = [
    path('payment_init/<int:course_id>/', views.payment_init, name = 'payment_init'),
    path('processpayment/<int:course_id>/', views.processpayment, name = 'processpayment'),
    path('exam_payment_init/<int:exam_id>/', views.exam_payment_init, name = 'exam_payment_init'),
    path('exam_processpayment/<int:exam_id>/', views.exam_processpayment, name = 'exam_processpayment'),
    path('canceled/', views.payment_canceled, name='canceled'),
]


