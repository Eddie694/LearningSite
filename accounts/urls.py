from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from accounts.views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

app_name = 'accounts'

urlpatterns = [
    path('login_user/', views.login_user, name = 'login'),
    path('signup_user/', views.signup_user, name = 'signup'),
    path('logout_user/', views.logout_user, name = 'logout_user'),
    path('bios/', views.bios, name = 'bios'),
    path('password_change/', views.password_change, name = 'password_change'),
    path('change_email/', views.change_email, name = 'change_email'),
    path('verify_email/', views.verify_email, name = 'verify_email'),
    
   #reset password
    path('accounts/password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]




