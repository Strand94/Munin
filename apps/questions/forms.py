from django import forms

from apps.questions.models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'text')


class BootstrapQuestionForm(QuestionForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapQuestionForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })