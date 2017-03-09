from django.db import models
from apps.registration.models import User
import datetime

class Question(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250, default='')
    asked_question = models.ForeignKey(User)

class Course(models.Model):
    name = models.CharField(max_length=50)
    course_id = models.CharField(max_length=7)
    lecturer = models.ForeignKey(User)
    YEAR_CHOICES = []
    for r in range(2000, (datetime.datetime.now().year + 2)):
        YEAR_CHOICES.append((r, r))
    year = models.IntegerField(choices=YEAR_CHOICES)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.course_id + ' - ' + self.name


class Feedback(models.Model):
    text = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    timestamp = models.TimeField(default=datetime.datetime.now())
    