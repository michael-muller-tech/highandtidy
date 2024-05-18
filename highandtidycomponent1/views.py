from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tasks
from .forms import TaskForm


def sayhello(request):
    data = {'name': 'Michael'}
    return render(request, 'highandtidycomponent1/hello.html', data)

def guest(request):
    return render(request, 'highandtidycomponent1/guest.html')

def signup(request):
    return render(request, 'highandtidycomponent1/signup.html')

def login(request):
    return render(request, 'highandtidycomponent1/login.html')

def addtask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task_instance = form.save(commit=False) #Create instance
            task_instance.save() #Save instance
            return HttpResponseRedirect("/thanks/")
    else:
        form = TaskForm()
    return render(request, "highandtidycomponent1/addtask.html", {"form": form})

def test5(request):
    return render(request, 'highandtidycomponent1/test5.html')

def thanks(request):
    return render(request, 'thanks.html')