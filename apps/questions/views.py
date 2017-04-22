from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from apps.questions.models import Question, Answer
from apps.courses.models import Course
from apps.questions.forms import BootstrapQuestionForm
import datetime


def subject_dashboard(request, pk):
    course = get_object_or_404(Course, pk=pk)
    question_list = Question.objects.filter(course=course).order_by('-timestamp')[0:3]
    top = Question.objects.filter(course=course).order_by('-vote_score', '-timestamp')[0:3]
    return render(request, 'staticpages/../../templates/questions/subject_dashboard.html',
                  {'subject': course,'top': top, 'questions': question_list})


def subject_questions(request, pk):
    course = get_object_or_404(Course, pk=pk)
    question_list = Question.objects.filter(course=course).order_by('-timestamp')
    return render(request, 'staticpages/../../templates/questions/subject_questions.html',
                  {'subject': course, 'questions': question_list})


def question(request, pk):
    question_asked = get_object_or_404(Question, pk=pk)
    answer_list = Answer.objects.filter(question=question_asked).order_by('-vote_score', '-timestamp')
    if request.method == 'POST':
        user = request.user
        if 'upvote_question' in request.POST:
            question_pk= request.POST.get('upvote_question')
            question = Question.objects.get(pk=question_pk)
            if question.votes.exists(user.id):
                question.votes.delete(user.id)
            else:
                question.votes.up(user.id)
            return HttpResponseRedirect("#")

        elif 'downvote_question' in request.POST:
            question_pk = request.POST.get('downvote_question')
            question = Question.objects.get(pk=question_pk)
            question.votes.down(user.id)
            return HttpResponseRedirect("#")

        elif 'add_answer' in request.POST:
            answer_text = request.POST.get('add_answer_box')
            if not answer_text:
                print("du har ingen svar, din fjott!")
            else:
                question_pk = request.POST.get('add_answer')
                question = Question.objects.get(pk=question_pk)
                answer = Answer.objects.create(question=question)
                answer.text = answer_text
                answer.user = request.user
                answer.timestamp = datetime.datetime.now()
                answer.save()
                print("Ask question activated")
                print(answer_text)

    return render(request, 'staticpages/../../templates/questions/question_page.html',
                  {'question': question_asked, 'answers': answer_list})


def new_question(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = BootstrapQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            if(request.POST.get("anonymous")):
                question.user = None
            else:
                question.user = request.user
            question.course = course
            question.timestamp = datetime.datetime.now()
            question.save()
            return HttpResponseRedirect("/course/question/"+str(question.pk))

    form = BootstrapQuestionForm(request.POST)
    return render(request, "staticpages/../../templates/questions/question_form.html", {'form': form})


def myQuestions(request):
    user=request.user
    myQues=Question.objects.filter(user=user)
    numOfQuestions=len(myQues)
    return render(request, 'questions/../../templates/questions/my_questions.html', {'antall':numOfQuestions, 'my_Questions': myQues})