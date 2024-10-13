from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test_dash, name='test_dash'),  # Add URL for Dash charts
]

