from django.db import models

class Report(models.Model):
    name = models.CharField(max_length = 30)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='reports/')
    timestamp = models.DateTimeField(auto_now_add=True)


class HomeNurse(models.Model):
    name_of_patient = models.CharField(max_length = 30)
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(max_length = 20, choices = GENDER)
    address = models.TextField(max_length = 200)
    contact = models.CharField(max_length = 20)
    weeks_needed = models.CharField(max_length = 10)
    SERVICE_TYPES = (
        ('nursing care', 'Nursing care'),
        ('physiotherapy', 'Physiotherapy')
    )
    service_needed = models.CharField(max_length = 20, choices = SERVICE_TYPES)
    emergency_contact = models.CharField(max_length = 20)
    name = models.CharField(max_length = 30)
    #health details of patients
    medical_conditons = models.TextField(max_length = 200)
    current_medications = models.TextField(max_length = 200)


class Ambulance_service(models.Model):
    name = models.CharField(max_length = 20)
    address = models.TextField(max_length = 200)
    contact = models.CharField(max_length = 20)
    direction_instructions = models.TextField(max_length = 200)


class Feedback(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    message = models.TextField(max_length = 200)

class Inventory(models.Model):
    location=models.CharField(max_length=100)
    total_strength=models.CharField(max_length=500)
    available_units=models.CharField(max_length=500)
    last_updated=models.DateTimeField(auto_now=True)
