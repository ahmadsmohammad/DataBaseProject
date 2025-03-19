from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# User Model with Roles
class User(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Patient', 'Patient'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Patient')

    # Fix conflicts with Django's built-in User model
    groups = models.ManyToManyField(Group, related_name="hospital_users", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="hospital_users_permissions", blank=True)

    def get_fields(self):
        return [self.id, self.username, self.role]

# Patient Model
class Patient(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def get_fields(self):
        return [self.id, self.user.username, self.dob, self.gender, self.phone, self.address]

# Doctor Model
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    def get_fields(self):
        return [self.id, self.user.username, self.specialty, self.phone, self.email]

# Nurse Model
class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)

    def get_fields(self):
        return [self.id, self.user.username, self.department, self.phone]

# Room Model
class Room(models.Model):
    ROOM_TYPES = (
        ('General', 'General'),
        ('ICU', 'ICU'),
        ('Operation Theater', 'Operation Theater'),
        ('Private', 'Private'),
    )
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    capacity = models.IntegerField()
    current_occupancy = models.IntegerField(default=0)

    def get_fields(self):
        return [self.id, self.room_number, self.room_type, self.capacity, self.current_occupancy]

# Admission Model (Tracks which patient is in which room)
class Admission(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    admission_date = models.DateTimeField(auto_now_add=True)
    discharge_date = models.DateTimeField(null=True, blank=True)

    def get_fields(self):
        return [self.id, self.patient.user.username, self.room.room_number, self.admission_date, self.discharge_date]

# Appointment Model
class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')

    def get_fields(self):
        return [self.id, self.patient.user.username, self.doctor.user.username, self.appointment_date, self.status]

# Medical Record Model
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    prescription = models.TextField()
    visit_date = models.DateTimeField(auto_now_add=True)

    def get_fields(self):
        return [self.id, self.patient.user.username, self.doctor.user.username, self.diagnosis, self.prescription, self.visit_date]
