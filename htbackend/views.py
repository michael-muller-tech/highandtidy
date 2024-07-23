from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Log

def log_list(request):
    logs = Log.objects.all().order_by('-timestamp'),

