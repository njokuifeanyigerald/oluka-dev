from django.db import models
from students.models import Student
from django.contrib.auth import get_user_model

User = get_user_model()

class Staff(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=100)
    department_id = models.ForeignKey("Department", on_delete=models.SET_NULL, blank=True,null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.staff_name

class Subject(models.Model):
    subjects = models.CharField(max_length=100)

    def __str__(self):
        return self.subjects
class Software1(models.Model):
    level = models.CharField(max_length=100, default="js")
    software = models.ManyToManyField(Subject)
   

class Department(models.Model):
    class CourseType(models.TextChoices):
        computer_hardware_engineering = "computer hardware engineering"
        computer_software_engineering ="computer software engineering "
        networking_and_system_security = "networking and system security"
    department = models.CharField(max_length=100, choices=CourseType.choices)
    # subject = models.ManyToManyField(Subject)

    
    def __str__(self):
        return self.department    


class Brochure(models.Model):
    email = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=5)

    def __str__(self):
        return self.department


