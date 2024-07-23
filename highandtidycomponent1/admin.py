from django.contrib import admin

from .models import Tasks, Households, Users, Assignment

# Register your models here.
admin.site.register(Households)
admin.site.register(Users)
admin.site.register(Tasks)
admin.site.register(Assignment)

