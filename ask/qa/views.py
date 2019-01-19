"""from django.shortcuts import render
from django.http import HttpResponse

def test(request, *args, **kwargs):
       return HttpResponse('OK')
"""
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login

from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm



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
    #paginator.baseurl = '/blog/all_posts/?page='
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
    #paginator.baseurl = '/blog/all_posts/?page='
    page = paginator.page(page)  # Page
    return render(request, 'pages.html', {
    'title': 'Popular',
    'paginator': paginator,
    'posts': page.object_list,
    'page': page,
    'user': request.user,
    'session': request.session,
})


def Seequestion(request, num,):
    try:
        question = Question.objects.get(id=num)
    except question.DoesNotExist:
        raise Http404
'''
    try:
        answer = Answer.objects.filter(question__id=num)
    except answer.DoesNotExist:
        answer = None
'''
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            ##form._user = request.user
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


def ask_me(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            q = form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'post_question.html', {'form':form})
