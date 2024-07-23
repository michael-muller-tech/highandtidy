from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Log

class LogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'level', 'message')
    list_filter = ('level', 'timestamp')
    search_field = ('message')