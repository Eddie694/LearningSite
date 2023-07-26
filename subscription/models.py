
import secrets
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


from acetelapp.models import Course, Exam

# Create your models here.

class RegisteredCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    currency = models.CharField(max_length=50, null=True, default='NGN')
    email = models.EmailField()
    amount = models.PositiveBigIntegerField()
    paystack_ref = models.CharField(max_length=15, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
        
    class Meta:
        ordering = ('-date_created',)
    
    def __str__(self):
        return f"user: {self.user.email} ({self.user.first_name}) - amount: {self.amount}"
    
    def get_amount(self):
        return self.amount
    
    def save(self, *args, **kwargs):
        while not self.paystack_ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_paystack_ref = RegisteredCourse.objects.filter(paystack_ref=ref)
            if not object_with_similar_paystack_ref:
                self.paystack_ref = ref
        super().save(*args, **kwargs)

    

class RegisteredExam(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    currency = models.CharField(max_length=50, null=True, default='NGN')
    email = models.EmailField()
    amount = models.IntegerField()
    paystack_ref = models.CharField(max_length=15, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
   

    class Meta:
        ordering = ('-date_created',)
    
    def __str__(self):
        return f"user: {self.user.email} ({self.user.first_name}) - amount: {self.amount}"
    
    def get_amount(self):
        return self.amount
    
    def save(self, *args, **kwargs):
        while not self.paystack_ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_paystack_ref = RegisteredExam.objects.filter(paystack_ref=ref)
            if not object_with_similar_paystack_ref:
                self.paystack_ref = ref
        super().save(*args, **kwargs)



        