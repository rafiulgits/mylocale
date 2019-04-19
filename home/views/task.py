from account.models import Account

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse

from generic.variables import LOGIN_URL

from home.models import Task, UserTaskReport
from home.forms import TaskForm, TaskUpdateForm


def view(request,task_id):
	try:
		task = Task.objects.get(id=task_id)

		report  = UserTaskReport.objects.filter(task_id=task_id)

		context = {}
		context['task'] = task
		context['issue_list'] = task.issues.all()

		if request.user.is_authenticated:
			user_report = UserTaskReport.objects.filter(user_id=request.user.id).filter(task_id=task_id).first()
			if user_report:
				context['user_report'] = True


		return render(request, 'home/task/view.html', context)

	except ObjectDoesNotExist as e:
		return HttpResponse('invalid request')




def list(request):
	context = {}
	task_list = Task.objects.all()
	context['task_list'] = task_list

	return render(request, 'home/task/list.html', context)



@login_required(login_url=LOGIN_URL)
def create(request):
	if not request.user.is_staff:
		HttpResponse('access denied')

	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			task = form.save()
			return HttpResponse('task created')

	form = TaskForm()
	context = {}
	context['form'] = form


	return render(request, 'home/task/create.html',context)



@login_required(login_url=LOGIN_URL)
def update(request, task_id):
	if not request.user.is_staff:
		HttpResponse('access denied')

	try:
		task = Task.objects.get(id=task_id)
		if request.method == 'POST':
			form = TaskUpdateForm(request.POST, task=task)
			if form.is_valid():
				task.title = form.cleaned_data['title']
				task.description = form.cleaned_data['description']
				task.save()
			return redirect('/task/'+task_id+'/')

		form = TaskUpdateForm(task=task)
		context = {}
		context['form'] = form


		return render(request, 'home/task/update.html', context)

	except ObjectDoesNotExist as e:
		pass

	return HttpResponse('invalid request')