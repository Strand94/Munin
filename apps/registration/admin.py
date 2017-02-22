from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Course


class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
            'middle_name',
            'image',
            'role',
            'school',
        )}),
    )

admin.site.register(User, MyUserAdmin)
admin.site.register(Course)
