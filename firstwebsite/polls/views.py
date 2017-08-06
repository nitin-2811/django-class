
# Create your views here.
from django.http import HttpResponse

from django.template import loader

from .models import Question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
def result(request,question_id):
    return HttpResponse("You r looking at results of %s"%question_id)
def vote(request,question_id):
    return HttpResponse("You voted for %s"%question_id)
