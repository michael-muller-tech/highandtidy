from django.db import models


class Households(models.Model):
    household_id = models.AutoField(primary_key=True)
    household_name = models.CharField(max_length=45, default=0)

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
    household_id = models.ForeignKey(Households, on_delete=models.CASCADE, default=False)

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
    
class Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    household = models.ForeignKey(Households, on_delete = models.CASCADE)
    assignment_name = models.CharField(max_length=45)

    def __str__(self):
        return self.assignment_name
    
    def save(self, *args, **kwargs):
        #Auto-populate assignment name with the name of the associated task 
        self.assignment_name = self.task.name
        super().save(*args, **kwargs)

