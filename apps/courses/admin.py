from django.contrib import admin
from .models import *

class CourseInfoAdmin(admin.ModelAdmin):
    filter_horizontal = ('students', )

admin.site.register(CourseInfo, CourseInfoAdmin)

admin.site.register(Course)