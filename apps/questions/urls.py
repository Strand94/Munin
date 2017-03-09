from django.conf.urls import url

from apps.questions import views
from apps.questions.views import *

urlpatterns = [
    url(r'^$', AskQuestion, name="questions"),
]