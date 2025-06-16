from django import forms
from .models import Tasks
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'is_custom']

class DeleteTaskForm(forms.Form):
        taskid = forms.IntegerField(widget=forms.HiddenInput())
        fields = ['taskid']

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'is_custom']

class AuthenticationForm (forms.ModelForm):
     class Meta:
        model = User
        fields = ['username', 'password']