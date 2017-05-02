from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,User
#
# class Student(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
#     department = models.ForeignKey(to=Department,related_name="studies_in",null=True, blank=True)
#     semester = models.CharField(max_length=50,choices=(('S1','Semester I'),('S2','Semester II'),('S3','Semester III'),('S4','Semester IV'),('S5','Semester V'),('S6','Semester VI'),('S7','Semester VII'),('S8','Semester VIII')),default=1)
#     date_of_registration = models.DateField()
#     name = models.CharField(max_length=30)
#     name_of_parent = models.CharField(max_length=30)
#     address = models.TextField(max_length=100)
#     Academic_History = models.ForeignKey(to=Academic_History,related_name="examdetails",null=True, blank=True)
#     Whether_eligible_for_registration = models.CharField(max_length=50,choices=((1,'No'),(2,'Yes')),default=2)
#     Hosteler_or_dayscholar = models.CharField(max_length=10,choices=(('D','Dayscholar'),('H','Hosteler')),default='D')
#     name_of_hostel = models.CharField(max_length=50,null=True,blank=True)
#
#     def __str__(self):
#         return self.user
TYPE_CHOICES = (
    ('F', 'Faculty'),
    ('S', 'Student'),
)
BRANCH_CHOICES = (
    ('CS', 'CS'),
    ('CE', 'CE'),
    ('PE', 'PE'),
    ('ME', 'ME'),
    ('EC', 'EC'),
)
SEX_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
    ('o', 'Others/Undefined'),
)
class User(models.Model):
    regNo = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    dob = models.DateField(max_length=16)
    department = models.CharField(max_length=2, choices=BRANCH_CHOICES)
    usertype = models.CharField(max_length=10, choices=TYPE_CHOICES) #F for Faculty and S for Student
    phoneNo = models.IntegerField()

    def __str__(self):
        return self.name
    #Academic_History = models.ForeignKey(to=Academic_History,related_name="examdetails",null=True, blank=True)
#
# class Attendance(models.Model):
#     student = models.ForeignKey(to=Student,related_name="attends",null=True, blank=True)
#     subject = models.ForeignKey(to=Subject,related_name="attended",null=True, blank=True)
#     month = models.DateField()
#     hours_in_total = models.IntegerField()
#     hours_attended = models.IntegerField()
#
#     def __str__(self):
#         return self.student
class Attendance(models.Model):
    regNo = models.ForeignKey(User, on_delete=models.CASCADE)
    term1 = models.IntegerField()
    term2 = models.IntegerField()

class Mark(models.Model):
    regNo = models.ForeignKey(User, on_delete=models.CASCADE)
    en14401 = models.IntegerField()
    en14402 = models.IntegerField()
    en14403 = models.IntegerField()
    en14404 = models.IntegerField()
    en14405 = models.IntegerField()
    en14406 = models.IntegerField()
