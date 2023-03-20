from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    GENDER_CHOICES =(
        ('F','F'),
        ('M','M'),
    )
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES , blank=True , null=True)
    phone = models.CharField(max_length=15 , blank=True , null=True)

