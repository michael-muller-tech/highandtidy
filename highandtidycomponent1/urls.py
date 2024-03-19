from django.urls import path
from . import views

#URLCONFMODEL
urlpatterns = [
    path('hello/', views.sayhello),
    path('guest/', views.guest),
    path('login/', views.login),
    path('signup/', views.signup),
    path('addtask/', views.addtask),
    path('test5/', views.test5),
    path('thanks/', views.thanks),
]