from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    path('log/', views.log_list, name='log_view'),  # Example view for logs
    # Add more URL patterns as needed
]
