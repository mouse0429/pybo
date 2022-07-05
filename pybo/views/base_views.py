from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

def index(request):
  page = request.GET.get('page', '1')
  question_list = Question.objects.order_by('-create_date')
  paginator = Paginator(question_list, 10)
  max_index = len(paginator.page_range)
  page_obj = paginator.get_page(page)
  context = {'question_list': page_obj, 'max_index': max_index}
  return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  context = {'question': question}
  return render(request, 'pybo/question_detail.html', context)