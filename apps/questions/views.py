from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.questions.models import Question

# Create your views here.

def Questions (request):
    if request.method=='POST':
        if 'delete_question' in request.POST:
            delete = request.POST.get('delete_question')
            q_to_delete = Question.objects.filter(pk=delete)
            q_to_delete.delete()

        user = request.user
        allMyQuestions = Question.objects.filter(asked_question=user)
        return render(request, "questions/questions.html",
                      {'myQuestions': allMyQuestions})

    else:
        user = request.user
        allMyQuestions = Question.objects.filter(asked_question=user)
        return render(request,"questions/questions.html",
                      {'myQuestions': allMyQuestions})

def AskNewQuestion (request):
    return render(request, "questions/ask_new.html")

def YouAskedAQuestion (request):
        if request.method == 'POST':

            user = request.user
            question_text = request.POST.get('question_box', None)

            if question_text == '':
                return HttpResponseRedirect("/questions/ask_new_question")

            question = Question()
            question.question = question_text
            question.asked_question = user
            question.save()

            return render(request, "questions/you_asked_a_question.html",
                          {'myQuestion': question})
        else:
            return render(request, "questions/ask_new.html")