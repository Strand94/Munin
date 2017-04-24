from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import User
from django.shortcuts import render, HttpResponseRedirect, redirect, render_to_response


# Create your views here.
class Profile(LoginRequiredMixin, generic.DetailView):
    model = User
    slug_field = 'username'
    template_name = 'registration/profile.html'

@login_required()
def edit_user(request):
    user = request.user
    if request.method == 'POST':
        f_name=request.POST.get("first_name")
        m_name=request.POST.get("middle_name")
        l_name=request.POST.get("last_name")
        if user.first_name!=f_name:
            user.first_name=f_name
        if user.middle_name!=m_name:
            user.middle_name=m_name
        if user.last_name!=l_name:
            user.last_name=l_name

        user.save()
        return HttpResponseRedirect(user.username)
    else:
        return render(request, 'registration/../../templates/registration/edit_user.html')