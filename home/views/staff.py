from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render, redirect, HttpResponse,Http404

from generic.variables import LOGIN_URL
from home.models import Task, Issue


@login_required(login_url=LOGIN_URL)
def panel(request):
	if not request.user.is_staff:
		return HttpResponse('access denied')

	context = {}

	return render(request, 'home/staff/panel.html', context)




@login_required(login_url=LOGIN_URL)
def open_tasklist(request):
	if not request.user.is_staff:
		return HttpResponse('access denied')

	context = {}

	return render(request, 'home/staff/open_tasklist.html', context)




@login_required(login_url=LOGIN_URL)
def close_tasklist(request):
	if not request.user.is_staff:
		return HttpResponse('access denied')

	context = {}

	return render(request, 'home/staff/close_tasklist.html', context)



@login_required(login_url=LOGIN_URL)
def open_issuelist(request):
	if not request.user.is_staff:
		return HttpResponse('access denied')

	context = {}

	return render(request, 'home/staff/open_issuelist.html', context)



@login_required(login_url=LOGIN_URL)
def progress_issuelist(request):
	if not request.user.is_staff:
		return HttpResponse('access denied')

	context = {}

	return render(request, 'home/staff/progress_issuelist.html', context)



@login_required(login_url=LOGIN_URL)
def close_issuelist(request):
	if not request.user.is_staff:
		return HttpResponse('access denied')

	context = {}

	return render(request, 'home/staff/close_issuelist.html', context)