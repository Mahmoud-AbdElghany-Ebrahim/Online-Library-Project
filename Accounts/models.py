from django.db import models


class Student(models.Model):
    Fname=models.CharField(max_length=25)
    Lname=models.CharField(max_length=25)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phoneNum=models.CharField(max_length=11)
    Bdate=models.DateField(auto_now_add=False,auto_now=False, blank=True)
    Role=(
        ("admin", "Admin"),
        ("student", "Student")
    )
    User=models.CharField(max_length=10, choices=Role)
    def __str__(self) :
        return self.Fname
    
class Admin(models.Model):
    Fname=models.CharField(max_length=25)
    Lname=models.CharField(max_length=25)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phoneNum=models.CharField(max_length=11)
    Bdate=models.DateField(auto_now_add=False,auto_now=False, blank=True)
    Role=(
        ("admin", "Admin"),
        ("student", "Student")
    )
    User=models.CharField(max_length=10, choices=Role, default="admin")
    def __str__(self) :
        return self.Fname

    

