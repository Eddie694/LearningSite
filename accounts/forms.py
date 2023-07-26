from django import forms
from django.contrib.auth.models import User
from .models import Profile 
from accounts.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _
from django.core.validators import RegexValidator

#customUserCreationForm
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.',
                                            widget=forms.TextInput(attrs={'class': 'form-control col-md-6'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.',
                                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=30, required=True, help_text='Required.',
                                            widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=30, required=True, help_text='Required.',
                                            widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    
    class Meta:
        model = User
        fields =('first_name','last_name', 'email', 'phone_number','password1','password2',)

        def clean_password1(self):
            password1 = self.cleaned_data.get('password1')
            password_validation.validate_password(password1, self.instance)
            return password1 


#creating update form for user
class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, 
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
    GENDER_CHOICES=(
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['gender', 'profile_pic']

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the form fields here (if needed)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm New Password'})

class ChangeEmailForm(UserChangeForm):
    email = forms.EmailField(label='New Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'New Email'}))


    class Meta:
        model = User
        fields = ('email',)