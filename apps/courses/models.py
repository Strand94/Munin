from django.db import models
from apps.registration.models import User
import datetime


class Course(models.Model):
    name = models.CharField(max_length=50)
    course_id = models.CharField(max_length=7)
    lecturer = models.ForeignKey(User)
    YEAR_CHOICES = []
    for r in range(2000, (datetime.datetime.now().year + 2)):
        YEAR_CHOICES.append((r, r))
    year = models.IntegerField(choices=YEAR_CHOICES)
    about = models.TextField(blank=True)
    examDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.course_id + ' - ' + self.name


class CourseInfo(models.Model):
    students = models.ManyToManyField(User, blank=True)
    course = models.OneToOneField(Course)

    def __str__(self):
        return self.course.name + ": studenter"