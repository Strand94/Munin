from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import BootstrapCourseForm
from .models import Course, CourseInfo
from apps.registration.models import User

@login_required
def lecture(request):
    user = request.user
    user_lectures = Course.objects.all().filter(lecturer=user)

    if request.method == 'POST':
        if 'delete' in request.POST:
            id = request.POST.get('delete')
            print(id)
            subject = Course.objects.filter(course_id__exact=id).delete()
            subject_info = CourseInfo.objects.filter(course=subject).delete()

    return render(request, "staticpages/../../templates/courses/lectures.html", {'lectures':user_lectures})

@login_required
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


    return render(request, "staticpages/../../templates/courses/subjects.html",
                  {'courses': available_courses.exclude(id__in=user_subjetcs_ids),
                   "mysubjects": user_subjetcs}
                  )

@login_required
def subject_participants(request, pk):
    course = get_object_or_404(Course, pk=pk)
    courseinfo = CourseInfo.objects.all().filter(course__course_id__exact=course.course_id).first()
    participants = courseinfo.students.all()
    return render(request, 'staticpages/../../templates/courses/subject_members.html', {"course":course, "participants":participants})


@login_required
def subject_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    this_course = CourseInfo.objects.all().filter(course__course_id__exact=course.course_id).first()
    user = request.user
    userRole = user.role
    user_school = User.objects.filter(username=user).first().school.pk
    user_subjetcs_ids = CourseInfo.objects.all().filter(students__username__contains=user.username).values('course_id')
    is_enrolled = user_subjetcs_ids.filter(course__course_id__exact=course.course_id)

    if request.method == 'POST':
        if 'remove' in request.POST:
            this_course.students.remove(user)

        elif 'add' in request.POST:
            this_course.students.add(user)

    return render(request, 'staticpages/../../templates/courses/subject_detail.html', {'subject': course, 'isEnrolled': is_enrolled
        ,'userRole': userRole})

@login_required
def subject_search(request):
    user = request.user
    user_subjects = CourseInfo.objects.all().filter(students__username__contains=user.username)
    user_school = User.objects.filter(username=user).first().school.pk
    available_courses = Course.objects.filter(lecturer__school=user_school)
    user_subjects_ids = CourseInfo.objects.all().filter(students__username__contains=user.username).values('course_id')

    return render(request, "staticpages/../../templates/courses/subject_search.html",
                  {'courses': available_courses.exclude(id__in=user_subjects_ids),
                   "mysubjects": user_subjects}
                  )

@login_required
def new_course(request):
    if request.method == "POST":
        form = BootstrapCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.lecturer = request.user

            colorlist = ['#f7c225', '#8a2ce8']
            number_of_questions = len(Course.objects.all())
            if (number_of_questions%3)==0:
                course.hexcolour=colorlist[0]
            elif (number_of_questions%3)==1:
                course.hexcolour=colorlist[1]

            course.save()
            courseinfo = CourseInfo.objects.create(course=course)
            courseinfo.save()
            return redirect('lecture')
    form = BootstrapCourseForm(request.POST)
    return render(request, "staticpages/../../templates/courses/course_form.html", {'form': form})


@login_required
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = BootstrapCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('lecture')
    else:
        form = BootstrapCourseForm(instance=course)
    return render(request, "staticpages/../../templates/courses/course_form.html", {'form': form})