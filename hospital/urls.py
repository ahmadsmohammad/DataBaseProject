from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PatientViewSet, DoctorViewSet, RoomViewSet, AppointmentViewSet,
    home, list_patients, list_doctors, list_rooms, list_appointments
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    # API Endpoints
    path('api/', include(router.urls)),  # All API routes are under `/api/`
    
    # Template Views
    path('', home, name='home'),
    path('patients/', list_patients, name='list_patients'),
    path('doctors/', list_doctors, name='list_doctors'),
    path('rooms/', list_rooms, name='list_rooms'),
    path('appointments/', list_appointments, name='list_appointments'),
]
