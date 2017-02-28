from registration.forms import RegistrationForm

from apps.registration.models import User


class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = User
        fields = ['username','email','school','first_name','middle_name','last_name','image']