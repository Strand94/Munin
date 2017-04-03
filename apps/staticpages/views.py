from django.shortcuts import render, get_object_or_404
from apps.registration.models import User
from apps.questions.models import Course, CourseInfo, Question
from apps.questions.forms import BootstrapCourseForm
from django.shortcuts import redirect


def FrontPage(request):
    return render(request, "frontpage.html")


def about(request):
    return render(request, "staticpages/about.html")


def contact(request):
    return render(request, "staticpages/contact.html")

def lecture(request):
    user = request.user
    user_lectures = Course.objects.all().filter(lecturer=user)

    return render(request, "staticpages/lectures.html", {'lectures':user_lectures})

def subject(request):
    user = request.user
    user_subjetcs = CourseInfo.objects.all().filter(students__username__contains=user.username)
    user_school = User.objects.filter(username=user).first().school.pk
    available_courses = Course.objects.filter(lecturer__school=user_school)
    user_subjetcs_ids = CourseInfo.objects.all().filter(students__username__contains=user.username).values('course_id')

    if request.method == 'POST':
        if 'remove' in request.POST:
            id = request.POST.get('remove')
            selected_subject = user_subjetcs.filter(course__course_id__exact=id).first()
            selected_subject.students.remove(user)

        elif 'add' in request.POST:
            id = request.POST.get('add')
            selected_subject = CourseInfo.objects.all().filter(course__course_id__exact=id).first()
            selected_subject.students.add(user)


    return render(request, "staticpages/subjects.html",
                  {'courses': available_courses.exclude(id__in=user_subjetcs_ids),
                   "mysubjects": user_subjetcs}
                  )

def subject_participants(request, pk):
    course = get_object_or_404(Course, pk=pk)
    courseinfo = CourseInfo.objects.all().filter(course__course_id__exact=course.course_id).first()
    participants = courseinfo.students.all()
    return render(request, 'staticpages/subject_members.html', {"course":course, "participants":participants})



def subject_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    this_course = CourseInfo.objects.all().filter(course__course_id__exact=course.course_id).first()
    user = request.user
    userRole = user.role
    user_subjetcs = CourseInfo.objects.all().filter(students__username__contains=user.username)
    user_school = User.objects.filter(username=user).first().school.pk
    available_courses = Course.objects.filter(lecturer__school=user_school)
    user_subjetcs_ids = CourseInfo.objects.all().filter(students__username__contains=user.username).values('course_id')
    is_enrolled = user_subjetcs_ids.filter(course__course_id__exact=course.course_id)

    if request.method == 'POST':
        if 'remove' in request.POST:
            this_course.students.remove(user)

        elif 'add' in request.POST:
            this_course.students.add(user)

    return render(request, 'staticpages/subject_detail.html', {'subject': course, 'isEnrolled': is_enrolled
        ,'userRole': userRole})

def subject_dashboard(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'staticpages/subject_dashboard.html', {'subject': course})

def subject_questions(request, pk):
    course = get_object_or_404(Course, pk=pk)
    questionlist = Question.objects.filter(course=course)
    return render(request, 'staticpages/subject_questions.html', {'subject': course, 'questions': questionlist})

def subject_search(request):
    user = request.user
    user_subjetcs = CourseInfo.objects.all().filter(students__username__contains=user.username)
    user_school = User.objects.filter(username=user).first().school.pk
    available_courses = Course.objects.filter(lecturer__school=user_school)
    user_subjetcs_ids = CourseInfo.objects.all().filter(students__username__contains=user.username).values('course_id')


    return render(request, "staticpages/subject_search.html",
                  {'courses': available_courses.exclude(id__in=user_subjetcs_ids),
                   "mysubjects": user_subjetcs}
                  )

def new_course(request):
    if request.method == "POST":
        form = BootstrapCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.lecturer = request.user
            course.save()
            courseinfo = CourseInfo.objects.create(course=course)
            courseinfo.save()
            return redirect('lecture')
    form = BootstrapCourseForm(request.POST)
    return render(request, "staticpages/course_form.html", {'form': form})

def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = BootstrapCourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            return redirect('lecture')
    else:
        form = BootstrapCourseForm(instance=course)
    return render(request, "staticpages/course_form.html", {'form': form})