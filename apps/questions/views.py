from django.shortcuts import render
from apps.questions.models import Question

# Create your views here.

def AskQuestion (request):
    return render(request,"questions.html")