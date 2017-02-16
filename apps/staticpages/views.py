from django.shortcuts import render

def FrontPage(request):
    return render(request, "frontpage.html")

def about(request):
    return render(request, "staticpages/about.html")

def contact(request):
    return render(request, "staticpages/contact.html")