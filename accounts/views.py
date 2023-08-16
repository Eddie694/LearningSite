from django.shortcuts import render, redirect
from accounts.forms import UpdateProfileForm, UpdateUserForm
from .forms import CustomPasswordChangeForm, ChangeEmailForm, CustomUserCreationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from accounts.forms import CustomPasswordResetForm, CustomPasswordResetConfirmForm
from acetelapp.views import courses, exams
from . models import Profile, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy




# Create your views here.
def signup_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request, 'Successfully registered, Login')
            return redirect('accounts:login')
        
    else:
        # If the request method is GET, create a new form instance
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form}) 
    

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('acetelapp:login_page')  # Replace 'dashboard' with your desired URL or view name
        else:
            messages.error(request, 'Email or Password Incorrect')
            return render(request, 'accounts/login.html', {'error': 'Invalid email or password.'})
    else:
        return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('acetelapp:index')


@login_required
def bios(request):
     
    if request.method == 'POST':
        user_form =UpdateUserForm(request.POST, instance = request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('accounts:bios')
    else:
        user_first_letter = request.user.first_name[0]
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
       
    context = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'user_first_letter': user_first_letter,
        'courses': courses,
        'exams': exams,
        'user_form': user_form,
        'profile_form': profile_form,
        
    }
    return render(request, 'accounts/bios.html', context)

@login_required
def password_change(request):
    user_first_letter = request.user.first_name[0]

    context = {
        'first_name': request.user.first_name,
        'user_first_letter': user_first_letter,
        'courses': courses,
        'exams': exams,
    }
    return render(request, 'accounts/password_change.html', context)


@login_required
def verify_email(request):
    user_first_letter = request.user.first_name[0]
    
    context = {
        'first_name': request.user.first_name,
        'user_first_letter': user_first_letter,
        'courses': courses,
        'exams': exams,
    }
    return render(request, 'accounts/verify_email.html', context)


@login_required
def password_change(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password was successfully changed.')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomPasswordChangeForm(request.user)
        
        context = {
        'first_name': request.user.first_name,
        'user_first_letter':request.user.first_name[0],
        'form': form,  
    }

    return render(request, 'accounts/password_change.html', context)


@login_required
def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your email address has been updated.')
            return redirect('accounts:change_email')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ChangeEmailForm(instance=request.user)

        context = {
        'first_name': request.user.first_name,
        'user_first_letter':request.user.first_name[0],
        'form': form,  
    }

    return render(request, 'accounts/change_email.html', context)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('accounts:password_reset_done')
    
    


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')
    form_class = CustomPasswordResetConfirmForm

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'


