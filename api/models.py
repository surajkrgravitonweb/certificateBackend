from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    course_duration = models.IntegerField()
    certificate_issue_date = models.DateField()

    def _str_(self):
        return self.name


    


class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email

from django.db import models

from django.db import models

class Certificate(models.Model):
    student_id = models.CharField(max_length=50)
    student_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    certificate_issue_date = models.DateField()

class Grade(models.Model):
    certificate = models.ForeignKey(Certificate, related_name='grades', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100,null=True, blank=True)
    marks_obtained = models.CharField(max_length=100,null=True, blank=True)
    minimum_marks = models.CharField(max_length=100,null=True, blank=True)
    maximum_marks = models.CharField(max_length=100,null=True, blank=True)  # Assuming this can be optional
