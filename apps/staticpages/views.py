from django.shortcuts import render, get_object_or_404
from apps.courses.models import Course, CourseInfo
from apps.registration.models import User


def FrontPage(request):
    return render(request, "frontpage.html")


def about(request):
    return render(request, "staticpages/about.html")


def contact(request):
    return render(request, "staticpages/contact.html")
