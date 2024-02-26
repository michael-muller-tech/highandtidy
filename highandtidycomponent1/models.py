from django.db import models

class Users(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.EmailField(max_length=100)
    # Use AutoField as primary key
    userid = models.AutoField(primary_key=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    tasks_completed = models.IntegerField(default=0)
    tasks_created = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    householdid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Tasks(models.Model):
    # Use AutoField as primary key
    taskid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=200, null=True, blank=True)
    is_custom = models.BooleanField(default=False)
    task_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Householdtasks(models.Model):
    # Use AutoField as primary key
    householdtaskid = models.AutoField(primary_key=True)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    createdby = models.ForeignKey(Users, on_delete=models.CASCADE)
    times_completed = models.IntegerField(default=0)

    def __str__(self):
        return self.task.name
