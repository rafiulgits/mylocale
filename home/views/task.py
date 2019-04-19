from account.models import Account

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, Http404

from generic.variables import LOGIN_URL

from home.models import Task, UserTaskReport
from home.forms import TaskForm


def view(request,task_id):
	try:
		task = Task.objects.get(id=task_id)

		report  = UserTaskReport.objects.filter(task_id=task_id)

		context = {}
		context['task'] = task

		if request.user.is_authenticated:
			user_report = UserTaskReport.objects.filter(user_id=request.user.id).filter(task_id=task_id).first()
			if user_report:
				context['user_report'] = True


		return render(request, 'home/task/view.html', context)

	except ObjectDoesNotExist as e:
		return Http404('invalid request')




def list(request):
	context = {}
	task_list = Task.objects.all()
	context['task_list'] = task_list

	return render(request, 'home/task/list.html', context)



@login_required(login_url=LOGIN_URL)
def create(request):
	if not request.user.is_staff:
		Http404('access denied')

	form = TaskForm()
	context = {}
	context['form'] = form