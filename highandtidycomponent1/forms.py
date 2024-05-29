from django import forms
from .models import Tasks  

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'taskid']

class DeleteTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['taskid']