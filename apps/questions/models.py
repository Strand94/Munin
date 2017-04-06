from django.db import models
from apps.registration.models import User
from apps.courses.models import Course
from vote.models import VoteModel
import datetime


#blank = true for user indicates anonymous post.
class Question(VoteModel, models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=2500)
    user = models.ForeignKey(User, null=True, blank=True)
    course = models.ForeignKey(Course)
    timestamp = models.DateTimeField(default=datetime.datetime.now())

    def get_answers(self):
        number = Answer.objects.filter(Question=self).count()
        return number


class Answer(VoteModel, models.Model):
    text = models.CharField(max_length=2500)
    user = models.ForeignKey(User, null=True, blank=True)
    question = models.ForeignKey(Question)
    timestamp = models.DateTimeField(default=datetime.datetime.now())
