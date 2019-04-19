from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render, redirect, HttpResponse,Http404

from generic.variables import LOGIN_URL

from home.models import Task, Issue

from farmer.models import Crop, Event

def index(request):
	context = {}

	task_list = Task.objects.filter(is_running=True).order_by('-time_date')[:5]
	trending_issue = Issue.objects.filter(is_open=True).order_by('-time_date')[:10]
	recent_issue = Issue.objects.order_by('-time_date')[:10]

	context['task_list'] = task_list
	context['trending_issue'] = trending_issue
	context['recent_issue'] = recent_issue

	return render(request, 'home/manage/index.html', context)




def search(request):
	if request.method != 'POST':
		return Http404('invalid request')

	query = request.POST.get('query', None)
	context = {}

	# issue result
	issue_result =Issue.objects.annotate(
		search=SearchVector('user__name', 'title', 'body','location__address')
		).filter(search=query)

	# task result
	task_result = Task.objects.annotate(
		search=SearchVector('title', 'description') 
		).filter(search=query)

	# crop result
	crop_result = Crop.objects.annotate(
		search=SearchVector('name','description','user__name')
		).filter(search=query)


	# event result
	event_result = Event.objects.annotate(
		search=SearchVector('title','description', 'address','user__name')
		).filter(search=query)


	context['query'] = query
	context['issue_result'] = issue_result
	context['task_result'] = task_result
	context['crop_result'] = crop_result
	context['event_result'] = event_result

	return render(request, 'home/manage/search.html', context)




