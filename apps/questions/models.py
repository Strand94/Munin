from django.db import models
from apps.registration.models import User
from apps.courses.models import Course
from vote.models import VoteModel
import datetime
from django.shortcuts import get_object_or_404


#blank = true for user indicates anonymous post.
class Question(VoteModel, models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=2500)
    user = models.ForeignKey(User, null=True, blank=True)
    asked_by = models.CharField(max_length=40, default="None")
    course = models.ForeignKey(Course)
    timestamp = models.DateTimeField(default=datetime.datetime.now())

    def get_answers(self):
        answer_list = Answer.objects.filter(question=self)
        number = len(answer_list)
        return number

    def __str__(self):
        return self.title + ' - ' + self.course.course_id


class Answer(VoteModel, models.Model):
    text = models.CharField(max_length=2500)
    user = models.ForeignKey(User, null=True, blank=True)
    question = models.ForeignKey(Question)
    timestamp = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.question.pk) + ' - '
