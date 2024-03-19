from django import forms

class taskForm(forms.Form):
    taskname = forms.CharField(label="Your task", max_length=100)
    taskdescription = forms.CharField(label="Description of task", max_length=100)