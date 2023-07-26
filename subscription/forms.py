from django import forms
from .models import RegisteredCourse

class RegisteredCourseForm(forms.ModelForm):
    class Meta:
        model = RegisteredCourse
        fields = ['user','course', 'currency', 'email', 'amount', 'paystack_ref']

    def __init__(self, user_id=None, course=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the initial values for the 'user' and 'course' fields
        self.initial['user'] = user_id
        self.initial['course'] = course