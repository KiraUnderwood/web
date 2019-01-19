from django import forms

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=1024)
    text = forms.CharField()

    def clean(self):
        pass

    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q


class AnswerForm(form.Forms):
    text = forms.CharField()
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def clean(self):
        pass

    def save(self):
        a = Answer(**self.cleaned_data)
        a.save()
        return a
