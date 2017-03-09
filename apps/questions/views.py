from django.shortcuts import render
from apps.questions.models import Question

# Create your views here.

def Questions (request):
    return render(request,"questions/questions.html")

def AskNewQuestion (request):
    return render(request,"questions/ask_new.html")