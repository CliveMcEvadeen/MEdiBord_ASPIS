from django.db import models
from unittest import result
# from django.db import models 
from django.db.models import Sum
from django.utils import timezone
# from 
import re

# Create your models here.   
# class Class(models.Model):
#     level = models.CharField(max_length=250)
#     section = models.CharField(max_length=250)
#     status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default = 1)
#     date_created = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.level + ' - ' + self.section)

# # class Subject(models.Model):
# #     name = models.CharField(max_length=250)
#     status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default = 1)
#     date_created = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(auto_now=True)


    # def __str__(self):
    #     return self.name


# class Student(models.Model):
    
#     classI = models.ForeignKey(Class, on_delete= models.CASCADE)
#     student_id = models.CharField(max_length=16)
#     first_name = models.CharField(max_length=250)
#     stream=models.CharField(max_length=10)
#     middle_name = models.CharField(max_length=250, blank= True, null=True)
#     last_name = models.CharField(max_length=250)
#     gender = models.CharField(max_length=20, choices=(('Male','Male'),('Female','Female')), default = 1)
#     status = models.CharField(max_length=2, choices=(('1','South'),('2','North',), ('3', 'west'), ('4','North')), default = 1)
#     date_created = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(auto_now=True)
#     name = models.CharField(max_length=500, blank=True)

#     def save(self, *args, **kwargs):
#         self.name = f"{self.first_name} {self.middle_name} {self.last_name}".strip()
#         super().save(*args, **kwargs)

    # def student_name(self):
    #     # Concatenate first, middle, and last names
    #     full_name = self.first_name
    #     if self.middle_name:
    #         full_name += " " + self.middle_name
    #     full_name += " " + self.last_name
    #     return full_name

    # def __str__(self):
    #     # if self.student_id.startswith("U0") and str(len(self.student_id)==16) or (len(self.student_id==15)):
    #     return str(self.student_id + " - " + self.first_name + " " + (str(self.middle_name + " " + self.last_name)  if self.middle_name != '' else self.last_name ))
    #     # else:
        #     return str("invalid LIN number")

    # def get_name(self):
    #     return str(self.first_name + " " + (str(self.middle_name + " " + self.last_name)  if self.middle_name != '' else self.last_name ))

# class Result(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     semester = models.CharField(max_length=250,blank=True)
#     date_created = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.student} - {self.semester}"

#     def countSubjects(self):
#         try:
#             resultCount = Student_Subject_Result.objects.filter(result = self).count()
#         except:
#             resultCount = 0
#         return resultCount

#     def average(self):
#         try:
#             resultCount = Student_Subject_Result.objects.filter(result = self).count()
#             results = Student_Subject_Result.objects.filter(result = self).aggregate(Sum('grade'))['grade__sum']
#             if not results is None:
#                 average = results / resultCount
#         except Exception as err:
#             print(err)
#             average = 0
#         return average

# class Student_Subject_Result(models.Model):
#     result = models.ForeignKey(Result, on_delete= models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
#     grade = models.FloatField(default=0)

#     def __str__(self):
#         return f"{self.result} - {self.subject}"

# class SubjectDetail(models.Model):
#     # conslidated data

#     subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, default=1)
#     student=models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
#     c1 = models.FloatField(null=True)
#     c2 = models.FloatField(null=True)
#     c3 = models.FloatField(null=True)
#     c4 = models.FloatField(null=True)
#     final = models.FloatField(null=True)

class Student(models.Model):
    lin = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    stream = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    c1 = models.FloatField(null=True, blank=True)
    c2 = models.FloatField(null=True, blank=True)
    c3 = models.FloatField(null=True, blank=True)
    fs = models.FloatField(null=True, blank=True)
    avg = models.FloatField(null=True, blank=True)
    twenty_percent = models.FloatField(null=True, blank=True)
    eighty_percent = models.FloatField(null=True, blank=True)
    final_score = models.FloatField(null=True, blank=True)
    identifier = models.CharField(max_length=10, null=True, blank=True)
    achievement = models.CharField(max_length=50, null=True, blank=True)
    initials = models.CharField(max_length=10, null=True, blank=True)

    def calculate_avg(self):
        self.avg = (self.c1 + self.c2 + self.c3 + self.fs) / 4
        self.save()

    def determine_identifier(self):
        if 0 <= self.avg <= 0.8:
            self.identifier = "G"
        elif 0.9 <= self.avg <= 1.1:
            self.identifier = "F"
        elif 1.2 <= self.avg <= 1.4:
            self.identifier = "E"
        elif 1.5 <= self.avg <= 1.7:
            self.identifier = "D"
        elif 1.8 <= self.avg <= 2.0:
            self.identifier = "C"
        elif 2.1 <= self.avg <= 2.3:
            self.identifier = "B"
        elif 2.4 <= self.avg <= 2.6:
            self.identifier = "A"
        elif 2.7 <= self.avg <= 3.0:
            self.identifier = "A*"
        elif self.avg > 3.0:
            self.identifier = "TF"
        self.save()

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"

class Marks(models.Model):
    student_subject = models.ForeignKey(StudentSubject, on_delete=models.CASCADE)
    component_name = models.CharField(max_length=10)
    marks = models.FloatField()

    def __str__(self):
        return f"{self.student_subject.student.name} - {self.student_subject.subject.name} - {self.component_name}"

class SchoolDetails(models.Model):
    school_name = models.CharField(max_length=50)
    school_contact1 = models.CharField(max_length=10)
    school_contact2 = models.CharField(max_length=10)
    school_contact3 = models.CharField(max_length=10, blank=True, null=True)
    school_box_number = models.CharField(max_length=10)
    school_badge = models.ImageField(upload_to='school_badges/')

    def __str__(self):
        return self.school_name
    

class StudentsDataS1(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    student_name = models.CharField(max_length=100)
    lin = models.CharField(max_length=12)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    stream = models.CharField(max_length=10)
    
class StudentsDataS2(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    student_name = models.CharField(max_length=100)
    lin = models.CharField(max_length=12)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    stream = models.CharField(max_length=10)

class StudentsDataS3(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    student_name = models.CharField(max_length=100)
    lin = models.CharField(max_length=12)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    stream = models.CharField(max_length=10)

class StudentsDataS4(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    student_name = models.CharField(max_length=100)
    lin = models.CharField(max_length=12)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    stream = models.CharField(max_length=10)
