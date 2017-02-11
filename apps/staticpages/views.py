from django.shortcuts import render

def FrontPage(request):
    return render(request, "frontpage.html")