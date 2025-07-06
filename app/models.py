from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers



class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Divorced', 'Divorced'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]

    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    father_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Father Name')

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name='Gender')

    tazkira_number = models.CharField(max_length=50, unique=True, verbose_name='Tazkira Number')
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Phone Number')

    dob = models.DateField(null=True, blank=True, verbose_name='Date of Birth')
    marital_status = models.CharField(max_length=8, choices=MARITAL_STATUS_CHOICES, null=True, blank=True, verbose_name='Marital Status')
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, null=True, blank=True, verbose_name='Blood Group')

    province = models.CharField(max_length=100, null=True, blank=True, verbose_name='Province')
    district = models.CharField(max_length=100, null=True, blank=True, verbose_name='District')
    village = models.CharField(max_length=100, null=True, blank=True, verbose_name='Village')
    address_details = models.TextField(null=True, blank=True, verbose_name='Address Details')

    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='Email')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.tazkira_number})"
