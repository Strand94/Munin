from django.shortcuts import render
from apps.registration.models import Course, User

def FrontPage(request):
    return render(request, "frontpage.html")

def about(request):
    return render(request, "staticpages/about.html")

def contact(request):
    return render(request, "staticpages/contact.html")

def subject(request):
    user = request.user
    user_school = User.objects.filter(username=user).first().school.pk
    available_courses = Course.objects.filter(lecturer__school=user_school)
    return render(request, "staticpages/subjects.html",
                  {'courses': available_courses}
                  )