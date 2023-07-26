from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login_user/', views.login_user, name = 'login'),
    path('signup_user/', views.signup_user, name = 'signup'),
    path('logout_user/', views.logout_user, name = 'logout_user'),
    path('bios/', views.bios, name = 'bios'),
    path('password_change/', views.password_change, name = 'password_change'),
    path('change_email/', views.change_email, name = 'change_email'),
    path('verify_email/', views.verify_email, name = 'verify_email'),
]




