from django.conf.urls import url

from apps.questions import views
from apps.questions.views import *

urlpatterns = [
    url(r'^$', Questions, name="questions"),
    url(r'^ask_new_question$', AskNewQuestion, name="ask_new_question"),
    url(r'^your_question$', YouAskedAQuestion, name="your_question"),
]