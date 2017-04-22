"""munin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from apps.staticpages.views import *
from apps.questions.views import *
from apps.courses.views import *
from registration.backends.hmac.views import RegistrationView
from apps.registration.form import MyCustomUserForm

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^user/', include('apps.registration.urls'), name='accounts'),
    url(r'^accounts/register/$',
        RegistrationView.as_view(
          form_class=MyCustomUserForm
      ),
      name='registration_register',
      ),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^$', FrontPage, name="home"),
    url(r'^course/question/(?P<pk>[0-9]+)', question, name='question'),
    url(r'^about/', about, name="about"),
    url(r'^contact/', contact, name="contact"),
    url(r'^subjects/$', subject, name="subject"),
    url(r'^lectures/$', lecture, name="lecture"),
    url(r'^subjects/search$', subject_search, name="subject_search"),
    url(r'^subjects/(?P<pk>[0-9]+)/participants', subject_participants, name="subject_participants"),
    url(r'^subjects/(?P<pk>[0-9]+)/info', subject_detail, name="subject_detail"),
    url(r'^subjects/(?P<pk>[0-9]+)/dashboard', subject_dashboard, name="subject_dashboard"),
    url(r'^my_questions', myQuestions, name="my_questions"),
    url(r'^subjects/(?P<pk>[0-9]+)/questions/$', subject_questions, name="subject_questions"),
    url(r'^lectures/new/$', new_course, name='new_course'),
    url(r'^lectures/(?P<pk>[0-9]+)/edit/$', edit_course, name='edit__course'),
    url(r'^subjects/(?P<pk>[0-9]+)/questions/ask', new_question, name="ask_question"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

