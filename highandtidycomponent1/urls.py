from django.urls import path
from . import views


#URLCONFMODEL
urlpatterns = [
    path('/hello', views.sayhello())
]