from django import forms

from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('name', 'course_id','year', 'about', 'examDate')


class BootstrapCourseForm(CourseForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapCourseForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })