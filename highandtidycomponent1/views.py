from django.shortcuts import render
from django.http import HttpResponse


def sayhello(request):
    data = {'name': 'Michael'}
    return render(request, 'hello.html', data)
