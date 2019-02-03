from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=1024)
    text = forms.CharField()

    def clean(self):
        pass

    def save(self):
        q = Question(**self.cleaned_data)
        q.author_id = self._user.id
        q.save()
        return q


class AnswerForm(forms.Form):
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
        a.author_id = self._user.id
        a.save()
        return a

    
class sign_me(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('please enter user name')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('this user already exists')
        except User.DoesNotExist:
            pass
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('please enter your email')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('plase enter the password')
        self.raw_passeord = password
        return make_password(password)

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user


    


class log_me(forms.Form):
    username = forms.CharField( max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('please enter user name')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('please enter the password')
        return password

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('incorrect user name or password')
        if not user.check_password(password):
            raise forms.ValidationError('incorrect user name or password')  
