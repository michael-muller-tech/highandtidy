from django.shortcuts import render
from django.http import HttpResponse


def sayhello(request):
    data = {'name': 'Michael'}
    return render(request, 'hello.html', data)

def guest(request):
    return render(request, 'guest.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')