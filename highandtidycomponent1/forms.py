from django import forms
from .models import Tasks  

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'is_custom']

class DeleteTaskForm(forms.Form):
        taskid = forms.IntegerField(widget=forms.HiddenInput())
        fields = ['taskid']

class UpdateTaskForm(forms.Form):
     taskid = forms.IntegerField(widget=forms.HiddenInput())