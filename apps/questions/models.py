from django.db import models
from apps.registration.models import User
from apps.courses.models import Course
from vote.models import VoteModel
import datetime


class Question(VoteModel, models.Model):
    text = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    timestamp = models.DateTimeField(default=datetime.datetime.now())


class Answer(VoteModel, models.Model):
    text = models.CharField(max_length=250)
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    timestamp = models.DateTimeField(default=datetime.datetime.now())
