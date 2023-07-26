from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, phone_number, password, **extra_fields):
        # Validate the email and password
        if not email:
            raise ValueError('Email must be a valid email address')
        if not password:
            raise ValueError('Password must be a valid password')
       
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, first_name, last_name, email, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(first_name, last_name, email, phone_number, password, **extra_fields)



#Create CustomUser Modele here 
class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(db_index=True, unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    
    
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name', 'phone_number']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.first_name


class Profile(models.Model):
    #creating gender choices
    GENDER_CHOICES=(
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
   

    # Add any additional fields and methods as needed

    def __str__(self):
        return self.user.first_name
