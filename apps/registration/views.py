from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import User

# Create your views here.
class Profile(LoginRequiredMixin, generic.DetailView):
    model = User
    slug_field = 'username'
    template_name = 'registration/profile.html'
