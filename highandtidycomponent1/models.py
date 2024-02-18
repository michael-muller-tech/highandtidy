from django.db import models

# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length=45, null=True)
    lastname = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=100, null=True)
    userid = models.IntegerField(null=True)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    tasks_completed = models.IntegerField(null=True)
    tasks_created = models.IntegerField(null=True)
    isadmin = models.BooleanField(null=True)
    householdid = models.IntegerField(null=True)

    def __str__(self):
        return self.firstname

class Tasks(models.Model):
    taskid = models.IntegerField(null=True)
    name = models.CharField(max_length=45, null=True)
    description = models.CharField(max_length=200, null=True)
    iscustom = models.BooleanField(null=True)
    taskcreated = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
    

class Householdtasks(models.Model):
    taskid = models.IntegerField(null=True)
    taskname = models.CharField(max_length=45, null=True)
    createdby = models.CharField(max_length=45, null=True)
    timescompleted = models.IntegerField(null=True)

    def __str__(self):
        return self.taskname

