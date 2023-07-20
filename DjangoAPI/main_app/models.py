from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin 
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.

# User Manager model

class AppUserManager(BaseUserManager):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('An email is required')
        if not password:
            raise ValueError('A password is required')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('An email is required')
        if not password:
            raise ValueError('A password is required')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()
        return user

# Abstract Base User 
    # first name, last name, email, password, image
class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()
    def __str__(self):
        return self.username


# Link model
    # Platform - choice (codepen | codewars | dev.to | facebook | freeCodeCamp | Frontend Mentor | github | gitlab | hashnode | LinkedIn | Stack overflow | twitch | twitter | youtube)
        # Cannot be blank / null
    # Url - charfield
        # cannot be blank / null
    # Order - change link order on user profile : integer field default 0
    # User - foreign key to user model
class Link(models.Model):
    CODEPEN = 'CP'
    CODEWARS = 'CW'
    DEVTO = 'DT'
    FACEBOOK = 'FB'
    FREECODECAMP = 'FC'
    FRONTEND_MENTOR = 'FM'
    GITHUB = 'GH'
    GITLAB = 'GL'
    HASHNODE = 'HN'
    LINKEDIN = 'LI'
    STACK_OVERFLOW = 'SO'
    TWITCH = 'TC'
    TWITTER = 'TW'
    YOUTUBE = 'YT'
    PLATFORM_CHOICES = [
        (CODEPEN, 'Codepen'),
        (CODEWARS, 'Codewars'),
        (DEVTO, 'Dev.to'),
        (FACEBOOK, 'Facebook'),
        (FREECODECAMP, 'freeCodeCamp'),
        (FRONTEND_MENTOR, 'Frontend Mentor'),
        (GITHUB, 'GitHub'),
        (GITLAB, 'GitLab'),
        (HASHNODE, 'hashnode'),
        (LINKEDIN, 'LinkedIn'),
        (STACK_OVERFLOW, 'Stack Overflow'),
        (TWITCH, 'Twitch'),
        (TWITTER, 'Twitter'),
        (YOUTUBE, 'YouTube')
    ]
    platform = models.CharField(
        max_length=2,
        choices=PLATFORM_CHOICES,
    )
    url = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
