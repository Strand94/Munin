import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.staticpages.models import School
import datetime


# returns the path where users upload pictures
def user_folder(instance, filename):
    return os.path.join('users', instance.username, filename)


class User(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)
    #This makes the role of a user a choice between the following choices.
    ROLES = (
        ('S', 'Student'),
        ('P', 'Professor'),
        ('A', 'Admin'),
    )
    role = models.CharField(max_length=1, null=True, choices=ROLES, default='S')
    image = models.ImageField(upload_to=user_folder, default='placeholder-profile.jpg')
    school = models.ForeignKey(School, null=True)

    #Returns the full name of the user.
    def get_full_name(self):
        if self.middle_name:
            #This if-statement has been added by Oyvind to avoid whitespace before middle name if there is no first name.
            if self.first_name == '':
                first_name = self.middle_name

            else:
                first_name = self.first_name + ' ' + self.middle_name
        else:
            first_name = self.first_name
        if first_name == '' and self.last_name == '':
            return self.username
        #This if-statement  has been added by Oyvind to avoid whitespace behind first_name if there is no last name.
        if self.last_name == '':
            return first_name
        #This if-statement has been added by Oyvind to avoid whitespace before last_name if there is no first_name.
        if first_name == '':
            return self.last_name

        return first_name + ' ' + self.last_name

    def get_lecturers(self):
        if self.role == 'P':
            return True
        else: return False

    def __str__(self):
        return self.username