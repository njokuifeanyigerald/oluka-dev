from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image

User = get_user_model()


class Student(models.Model):
    class CourseType(models.TextChoices):
        Computer_Hardware_Engineering = "Computer Hardware Engineering"
        Computer_Software_Engineering ="Computer Software Engineering"
        Networking_and_System_Security = "Networking And System Security"

    class StateType(models.TextChoices):
        Abia ="Abia"
        Adamawa ="Adamawa"
        Akwa_Ibom ="Akwa Ibom"
        Anambra ="Anambra"
        Bauchi ="Bauchi"
        Bayelsa ="Bayelsa"
        Benue ="Benue"
        Borno ="Borno"
        Cross_River ="Cross River"
        Delta ="Delta"
        Ebonyi ="Ebonyi"
        Edo ="Edo"
        Ekiti ="Ekiti"
        Enugu= "Enugu"
        Gombe= "Gombe"
        Imo="Imo"
        Jigawa= "Jigawa"
        Kaduna= "Kaduna"
        Kano= "Kano"
        Katsina= "Katsina"
        Kebbi= "Kebbi"
        Kogi= "Kogi"
        Kwara ="Kwara"
        Lagos ="Lagos"
        Nasarawa = "Nasarawa"
        Niger = "Niger"
        Ogun = "Ogun"
        Ondo = "Ondo"
        Osun = "Osun"
        Oyo = "Oyo"
        Plateau = "Plateau"
        Rivers = "Rivers"
        Sokoto = "Sokoto"
        Taraba = "Taraba"
        Yobe = "Yobe"
        Zamfara = "Zamfara"
        Federal_Capital_Territory= "Federal Capital Territory"
    
    class CoursePlan(models.TextChoices):
        crash_course = "Crash Course"
        part_time ="Part Time"
        full_time = "Regular"

    class HighestLevelOfEducation(models.TextChoices):
        High_School_Diploma = "High School Diploma"
        Degree = "Degree"
        Masters = "Masters"
        ND= "ND"
        HND = "HND"
    
    class Gender(models.TextChoices):
       Male = "Male"
       Female = "Female"
    
    class Employment(models.TextChoices):
        employed = "Employed"
        umemployed = "UnEmployed"
        self_employed= "Self-Employed"
        student = "Student"
    
    class Relationship(models.TextChoices):
        Brother = "Brother"
        Sister = "Sister"
        Father = "Father"
        Mother = "Mother"
        Relative = "Relative"
    
    student_fname = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100 , blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_email = models.EmailField(max_length=100)
    image = models.ImageField(verbose_name='image',null=True, blank=True)
    student_address = models.CharField(max_length=100)
    student_phone = models.CharField(max_length=15)
    highest_level_of_education = models.CharField(max_length=100, choices=HighestLevelOfEducation.choices)
    dob = models.DateField(null=True)
    employment_status = models.CharField(max_length=100, choices=Employment.choices, null=True, blank=True)
    employer_name = models.CharField(max_length=100, null=True, blank=True)
    desired_course = models.CharField(max_length=100, null=True, blank=True )
    referal_code = models.CharField(max_length=100, null=True, blank=True )
    disability = models.BooleanField(default=False)
    gender = models.CharField(max_length=100, choices=Gender.choices, blank=True,null=True)
    state_of_origin = models.CharField(max_length=100, choices=StateType.choices)
    state_of_residence = models.CharField(max_length=100, choices=StateType.choices)
    city = models.CharField(max_length=100)
    course_of_choice = models.CharField(max_length=100, choices=CourseType.choices,blank=True, null=True)
    course_of_choice2 = models.CharField(max_length=100, choices=CourseType.choices,blank=True, null=True) 
    course_enrolled = models.BooleanField(default=False)
    course_plan = models.CharField(max_length=100, choices=CoursePlan.choices)
    nextOfKinFullName = models.CharField(max_length=100, blank=True)
    nextOfKinEmail = models.EmailField(max_length=100, blank=True)
    nextOfKinPhone = models.CharField(max_length=100, blank=True)
    nextOfKinAddress = models.CharField(max_length=100, blank=True)
    nextOfKinRelationship = models.CharField(max_length=100, choices=Relationship.choices, blank=True)


    def __str__(self):
        return self.student_email
    
    class Meta:
        verbose_name_plural = "student"

class Guardian(models.Model):
    class ParentStateType(models.TextChoices):
        Abia ="Abia"
        Adamawa ="Adamawa"
        Akwa_Ibom ="Akwa Ibom"
        Anambra ="Anambra"
        Bauchi ="Bauchi"
        Bayelsa ="Bayelsa"
        Benue ="Benue"
        Borno ="Borno"
        Cross_River ="Cross River"
        Delta ="Delta"
        Ebonyi ="Ebonyi"
        Edo ="Edo"
        Ekiti ="Ekiti"
        Enugu= "Enugu"
        Gombe= "Gombe"
        Imo="Imo"
        Jigawa= "Jigawa"
        Kaduna= "Kaduna"
        Kano= "Kano"
        Katsina= "Katsina"
        Kebbi= "Kebbi"
        Kogi= "Kogi"
        Kwara ="Kwara"
        Lagos ="Lagos"
        Nasarawa = "Nasarawa"
        Niger = "Niger"
        Ogun = "Ogun"
        Ondo = "Ondo"
        Osun = "Osun"
        Oyo = "Oyo"
        Plateau = "Plateau"
        Rivers = "Rivers"
        Sokoto = "Sokoto"
        Taraba = "Taraba"
        Yobe = "Yobe"
        Zamfara = "Zamfara"
        Federal_Capital_Territory= "Federal Capital Territory"

    class Relationship(models.TextChoices):
        Brother = "Brother"
        Sister = "Sister"
        Father = "Father"
        Mother = "Mother"
        Relative = "Relative"   
    guardian = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    parent_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    phone_no  = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=30)
    State = models.CharField(max_length=100, choices=ParentStateType.choices)
    relationship  = models.CharField(max_length=100, choices=Relationship.choices)

    def __str__(self):
        return self.email


class Admission(models.Model):
    student   = models.OneToOneField(Student, on_delete=models.CASCADE)
    admitted = models.BooleanField(default=False)

class JambUpload(models.Model):
    class Subject(models.TextChoices):
        English = "English"
        Mathematics = "Mathematics"
        Biology = "Biology"
        Physics = "Physics"
        Chemistry =  "Chemistry"  
    jamb_score = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True)
    reg_no = models.CharField(max_length=30)
    exam_No = models.CharField(max_length=30)
    centre_name = models.CharField(max_length=80)
    subject1 = models.CharField(max_length=20, choices=Subject.choices)
    subject2 = models.CharField(max_length=20, choices=Subject.choices)
    subject3 = models.CharField(max_length=20, choices=Subject.choices)
    subject4 = models.CharField(max_length=20, choices=Subject.choices)
    score1 = models.FloatField()
    score2= models.FloatField()
    score3 = models.FloatField()
    score4 = models.FloatField()

    def total(self):
        return self.score1 + self.score2 + self.score3 + self.score4

class WAEC(models.Model):
    waec = models.OneToOneField(Student,on_delete=models.CASCADE)
    result = models.ImageField(verbose_name='waec') 
    accept = models.BooleanField(default=False)

    def __str__(self):
        return "WAEC"

class StudentMessages(models.Model):
    to = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.message
    
    class Meta:
        verbose_name_plural = "Messages"
        