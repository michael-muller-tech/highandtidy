from django.db import models

# Create your models here.
class Log(models.Model):
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=100)
    LEFEL_CHOICES=[
        ('DEBUG', 'Debug'),
        ('INFO', 'Info'),
        ('WARNING', 'Warning'),
        ('ERROR', 'Error'),
        ('CRITICAL', 'Critical'),
    ]

def __str__(self):
    return f"[{self.timestamp}] {self.level}: {self.message}"