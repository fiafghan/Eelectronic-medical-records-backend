from django.urls import path
from .views import (
    HelloWorld,
    RegisterView,
    LoginView,
    PatientListCreateView,
    PatientRetrieveUpdateDestroyView
)

urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello_world'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='patient-detail'),

]