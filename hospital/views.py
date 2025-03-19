# Import required Django and DRF modules
from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, Doctor, Room, Appointment
from .serializers import PatientSerializer, DoctorSerializer, RoomSerializer, AppointmentSerializer

# API Views (KEEP THESE)
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

# New Template Views (For Frontend)
def home(request):
    sections = [
        {'name': 'Users', 'url': '/users/'},
        {'name': 'Patients', 'url': '/patients/'},
        {'name': 'Doctors', 'url': '/doctors/'},
        {'name': 'Nurses', 'url': '/nurses/'},
        {'name': 'Rooms', 'url': '/rooms/'},
        {'name': 'Admissions', 'url': '/admissions/'},
        {'name': 'Appointments', 'url': '/appointments/'},
    ]
    return render(request, 'index.html', {'sections': sections})

def list_patients(request):
    patients = Patient.objects.all()
    return render(request, 'list.html', {'title': 'Patients', 'columns': ['ID', 'Name', 'DOB', 'Gender', 'Phone'], 'data': patients})

def list_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'list.html', {'title': 'Doctors', 'columns': ['ID', 'Name', 'Specialty', 'Phone', 'Email'], 'data': doctors})

def list_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'list.html', {'title': 'Rooms', 'columns': ['ID', 'Room Number', 'Type', 'Capacity', 'Current Occupancy'], 'data': rooms})

def list_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'list.html', {'title': 'Appointments', 'columns': ['ID', 'Patient', 'Doctor', 'Date', 'Status'], 'data': appointments})
