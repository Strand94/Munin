from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.questions.models import Question

# Create your views here.

def Questions (request):
    return render(request,"questions/questions.html")

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