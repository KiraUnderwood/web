"""from django.shortcuts import render
from django.http import HttpResponse
def test(request, *args, **kwargs):
       return HttpResponse('OK')
"""
# Create your views here.

from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from qa.forms import AskForm, AnswerForm, sign_me, log_me
from qa.models import Question, Answer


def recent(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    Allquestions = Question.objects.all().order_by('-id')
    ##all_questions = all_questions.order_by('-id')
    ##limit = request.GET.get('limit', 10)
    ##page = request.GET.get('page', 1)
    paginator = Paginator(Allquestions, 10)
    # paginator.baseurl = '/blog/all_posts/?page='
    page = paginator.page(page)  # Page
    return render(request, 'pages.html', {
        'title': 'Latest',
        'paginator': paginator,
        'posts': page.object_list,
        'page': page,
        'user': request.user,
        'session': request.session,
    })


def popular(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    Allquestions = Question.objects.all().order_by('-rating')
    ##all_questions = all_questions.order_by('-rating')
    ##limit = request.GET.get('limit', 10)
    ##page = request.GET.get('page', 1)
    paginator = Paginator(Allquestions, 10)
    # paginator.baseurl = '/blog/all_posts/?page='
    page = paginator.page(page)  # Page
    return render(request, 'pages.html', {
        'title': 'Popular',
        'paginator': paginator,
        'posts': page.object_list,
        'page': page,
        'user': request.user,
        'session': request.session,
    })


def Seequestion(request, num, ):
    try:
        question = Question.objects.get(id=num)
    except question.DoesNotExist:
        raise Http404
    
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
           answ = form.save()
           url = question.get_url()
           return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': question.id})

    return render(request, 'one_question.html', {
        'question': question,
        'form': form,
        'user': request.user,
        'session': request.session,

    })

'''
    try:
        answer = Answer.objects.filter(question__id=num)
    except answer.DoesNotExist:
        answer = None
'''



def ask_me(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            q = form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'post_question.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = log_me(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username, password)
            user = authenticate(username=username, password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = log_me()
    return render(request, 'login.html', {'form': form,
                                          'user': request.user,
                                          'session': request.session, })


def signup_view(request):
    if request.method == "POST":
        form = sign_me(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.raw_password
            user = authenticate(username=username, password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = sign_me()
    return render(request, 'signup.html', {'form': form,
                                           'user': request.user,
                                           'session': request.session, })
