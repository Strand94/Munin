from django.shortcuts import render, get_object_or_404
from apps.registration.models import User
from apps.questions.models import Course, CourseInfo


def FrontPage(request):
    return render(request, "frontpage.html")


def about(request):
    return render(request, "staticpages/about.html")


def contact(request):
    return render(request, "staticpages/contact.html")


def subject(request):
    user = request.user
    user_subjetcs = CourseInfo.objects.all().filter(students__username__exact=user.username)
    user_school = User.objects.filter(username=user).first().school.pk
    available_courses = Course.objects.filter(lecturer__school=user_school)
    return render(request, "staticpages/subjects.html",
                  {'courses': available_courses, "mysubjects": user_subjetcs}
                  )


def subject_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'staticpages/subject_detail.html', {'subject': course})