from django.contrib import admin
from .models import *

# Register your models here.
class CourseInfoAdmin(admin.ModelAdmin):
    filter_horizontal = ('students', )

admin.site.register(CourseInfo, CourseInfoAdmin)
