from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question, Answer

def index(request):
  page = request.GET.get('page', '1')
  kw = request.GET.get('kw', '')
  question_list = Question.objects.order_by('-create_date')
  if kw:
    question_list = question_list.filter(
      Q(subject__icontains=kw) |
      Q(content__icontains=kw) |
      Q(answer__content__icontains=kw) |
      Q(author__username__icontains=kw) |
      Q(answer__author__username__icontains=kw)
    ).distinct()
  paginator = Paginator(question_list, 10)
  max_index = len(paginator.page_range)
  page_obj = paginator.get_page(page)
  context = {'question_list': page_obj, 'max_index': max_index, 'page': page, 'kw': kw}
  return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  page = request.GET.get('page', '1')
  order = request.GET.get('order', 'recommended')
  answer_list = Answer.objects.filter(question_id=question.id).annotate(voter_count=Count('voter')).order_by('-voter_count')
  if order == 'latest':
    answer_list = Answer.objects.filter(question_id=question.id).order_by('-create_date')
  elif order == 'create':
    answer_list = Answer.objects.filter(question_id=question.id).order_by('create_date')
  paginator = Paginator(answer_list, 10)
  max_index = len(paginator.page_range)
  page_obj = paginator.get_page(page)
  context = {'question': question, 'answer_list': page_obj, 'max_index': max_index, 'page': page, 'order': order}
  return render(request, 'pybo/question_detail.html', context)