from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    lin = models.CharField(max_length=14, unique=True)
    gender = models.CharField(max_length=10)
    stream = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    c1 = models.FloatField()
    c2 = models.FloatField()
    c3 = models.FloatField()
    fs = models.FloatField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"

class Marks(models.Model):
    student_subject = models.ForeignKey(StudentSubject, on_delete=models.CASCADE)
    component_name = models.CharField(max_length=10)  
    marks = models.FloatField()

    def __str__(self):
        return f"{self.student_subject} - {self.component_name}: {self.marks}"

class Descriptor(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    component_name = models.CharField(max_length=10)  
    descriptor = models.TextField()

    def __str__(self):
        return f"{self.subject.name} - {self.component_name}"

class Average(models.Model):
    student_subject = models.ForeignKey(StudentSubject, on_delete=models.CASCADE)
    component_name = models.CharField(max_length=10)  
    average = models.FloatField()

    def __str__(self):
        return f"{self.student_subject} - {self.component_name} Average: {self.average}"

class SchoolDetails(models.Model):
    school_name = models.CharField(max_length=50)
    school_contact1 = models.CharField(max_length=10)
    school_contact2 = models.CharField(max_length=10)
    school_contact3 = models.CharField(max_length=10, blank=True, null=True)
    school_box_number = models.CharField(max_length=10)
    school_badge = models.ImageField(upload_to='school_badges/')

    def __str__(self):
        return self.school_name

    # def __str__(self) -> str:
    #     return f"{self.}"