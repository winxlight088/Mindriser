from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=10, null=True, unique = True)
    USERNAME_FIELD = "phone_number" #custom use this field if the admin user needs to login gin from phone number or nay other field