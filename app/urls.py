from django.urls import path
from .views import HelloWorld, RegisterView

urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello_world'),
    path('register/', RegisterView.as_view(), name='register'),
]