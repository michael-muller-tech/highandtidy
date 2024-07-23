#Storing messages

from .models import Log
from django.contrib import messages

def log_message(message, level='INFO'):
    level = level.upper()

    if level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
        raise ValueError(f"Invalid log level: {level}")

    Log.objects.create(message=message, level=level)