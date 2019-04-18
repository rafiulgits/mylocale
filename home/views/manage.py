from django.shortcuts import render, redirect, HttpResponse

from home.models import Task, Issue

def index(request):
	context = {}

	task_list = Task.objects.filter(is_running=True).filter('-time_date')[:5]
	trending_issue = Issue.objects.filter('-vote').filter(is_open=True)[:10]
	recent_issue = Issue.objects.filter('-time_date')[:10]

	context['task_list'] = task_list
	context['trending_issue'] = trending_issue
	context['recent_issue'] = recent_issue

	return render(request, 'home/manage/index.html', context)