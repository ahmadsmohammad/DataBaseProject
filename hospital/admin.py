from django.contrib import admin
from .models import User, Patient, Doctor, Nurse, Room, Admission, Appointment, MedicalRecord

# Register your models here.
admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Room)
admin.site.register(Admission)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)