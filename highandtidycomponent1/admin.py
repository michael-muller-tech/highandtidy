from django.contrib import admin
from .models import Households, Tasks, Assignment

# Register your models here.
admin.site.register(Households)
admin.site.register(Tasks)
admin.site.register(Assignment)

