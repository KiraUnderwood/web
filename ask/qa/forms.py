from django import forms

from qa.models import Question,Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=1024)
    text = forms.CharField()

    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q



class AnswerForm(form.Forms):
    text = forms.CharField()
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        


    def save(self):
