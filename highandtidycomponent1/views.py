from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tasks
from .forms import TaskForm, DeleteTaskForm


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
    # Retrieve all tasks from the database
    tasks = Tasks.objects.all()
    
    form = TaskForm()
    delete_form = DeleteTaskForm()

    if request.method == "POST":
        if 'add_task' in request.POST:  # Check if the add task form is submitted
            form = TaskForm(request.POST)
            if form.is_valid():
                task_instance = form.save(commit=False)
                task_instance.save()
                return redirect('/addtask')

        elif 'delete_task' in request.POST:  # Check if the delete task form is submitted
            delete_form = DeleteTaskForm(request.POST)
            if delete_form.is_valid():
                taskid = delete_form.cleaned_data['taskid']
                Tasks.objects.filter(taskid=taskid).delete()
                return redirect('/addtask')
    
    else:
        form = TaskForm()
        delete_form = DeleteTaskForm()
    
    tasks = Tasks.objects.all()
    
    return render(request, "highandtidycomponent1/addtask.html", {"form": form, "delete_form": delete_form, "tasks": tasks})


def test5(request):
    return render(request, 'highandtidycomponent1/test5.html')

def thanks(request):
    return render(request, 'highandtidycomponent1/thanks.html')

def homepage(request):
    return render(request, 'highandtidycomponent1/homepage.html')