from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('resident', 'Resident'),
        ('staff', 'Staff')
    )
    #common fields
    user_type = models.CharField(max_length = 10, choices = USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length = 20, null = True)
    address = models.TextField(max_length = 250, null = True)
    #staff fields
    ROLES = (
        ('manager', 'Manager'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('caretaker', 'Caretaker'),
        ('cook', 'Cook'),
        ('driver', 'Driver')
    )
    role = models.CharField(max_length = 20, choices = ROLES)
    #resident fields
    blood_pressure = models.CharField(max_length = 10, null = True)
    diabetes = models.CharField(max_length = 10, null = True)
    cholesterol = models.CharField(max_length = 10, null = True)
    allergies = models.TextField(max_length = 100, null = True)
    chronic_conditions = models.TextField(max_length = 100, null = True)
    medications = models.TextField(max_length = 100, null = True)
    diet_details = models.TextField(max_length = 100, null = True)
    documents = models.FileField(null = True)
    emergency_contact = models.CharField(max_length = 20, null = True)
    name_of_person = models.CharField(max_length = 30, null = True)
    



