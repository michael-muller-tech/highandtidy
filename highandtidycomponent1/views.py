from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tasks
from .forms import TaskForm, DeleteTaskForm, UpdateTaskForm
from django.contrib import messages


def sayhello(request):
    data = {'name': 'Michael'}
    return render(request, 'hello.html', data)

def guest(request):
    return render(request, 'guest.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def crudtask(request):
    # Retrieve all tasks from the database
    tasks = Tasks.objects.all()
    
    form = TaskForm()
    delete_form = DeleteTaskForm()
    update_form = UpdateTaskForm()

    if request.method == "POST":
        if 'add_task' in request.POST:  # Check if the add task form is submitted
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('crud-redirect')

        elif 'delete_task' in request.POST:  # Check if the delete task form is submitted
            delete_form = DeleteTaskForm(request.POST)
            if delete_form.is_valid():
                taskid = delete_form.cleaned_data.get('taskid')
                try:
                    task = Tasks.objects.get(taskid=taskid)
                    task.delete()
                    messages.success(request, 'Task deleted successfully')
                except Tasks.DoesNotExist:
                    messages.error(request, 'Invalid form submission')


        elif 'update_task' in request.POST:
            taskid = request.POST.get('taskid')
            if taskid:
                return redirect('temp-update', pk=taskid)
         
             
        else:
           messages.error(request, 'Failed to delete task.')
    
    return render(request, "addtask.html", {"form": form, "tasks": tasks})

def temp_update(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    print(f"Task ID: {task.pk}, Name: {task.name}, Description: {task.description}, Is Custom: {task.is_custom}")
    

    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('crud-redirect')  
    else:
        form = UpdateTaskForm(instance=task)

    print(form['description'].value())  

    return render(request, 'temp_update.html', {'form': form, 'task': task})

def test5(request):
    return render(request, 'test5.html')

def thanks(request):
    return render(request, 'thanks.html')

def homepage(request):
    return render(request, 'homepage.html')