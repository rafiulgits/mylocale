from account.models import Account

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse

from generic.variables import LOGIN_URL

from home.models import Task, UserTaskReport
from home.forms import TaskForm, TaskUpdateForm, UserTaskReportForm


def view(request,task_id):
	try:
		task = Task.objects.get(id=task_id)

		user_report  = UserTaskReport.objects.filter(task_id=task_id)

		context = {}
		context['task'] = task
		context['issue_list'] = task.issues.all()

		if request.user.is_authenticated:
			report_obj = UserTaskReport.objects.filter(task_id=task_id, user_id=request.user.id).first()
			if request.method == 'POST':
				form = UserTaskReportForm(request.POST, report_obj=report_obj)
				if form.is_valid():
					if report_obj:
						report_obj.report = form.cleaned_data['report']
						report_obj.save()

					else:
						user_report = UserTaskReport(user=request.user, task=task)
						user_report.report = form.cleaned_data['report']
						user_report.save()
					return redirect('/task/'+task_id+'/')

			form = UserTaskReportForm(report_obj=report_obj)
			context['form'] = form



		total_satisfied_service = UserTaskReport.objects.filter(task_id=task_id).filter(report='St').count()
		total_poor_service = UserTaskReport.objects.filter(task_id=task_id).filter(report='Ps').count()
		total_no_service = UserTaskReport.objects.filter(task_id=task_id).filter(report='Ns').count()

		total = total_satisfied_service+total_poor_service+total_no_service

		if total != 0:
			satisfied = round(((total_satisfied_service*100)/total),2)
			poor = round(((total_poor_service*100)/total),2)
			no = round(((total_no_service*100)/total),2)

		else:
			satisfied = 0
			poor = 0
			no = 0

		context['satisfied'] = satisfied
		context['poor'] = poor
		context['no'] = no


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


@login_required(login_url=LOGIN_URL)
def close(request, task_id):
	if not request.user.is_staff:
		HttpResponse('access denied')

	try:
		task = Task.objects.get(id=task_id)
		issues = task.issues.all()

		for item in issues:
			item.is_open = False
			item.in_progress = False
			item.save()

		task.is_running = False
		task.save()

		return redirect('/task/'+task_id+'/')

	except ObjectDoesNotExist as e:
		pass

	return HttpResponse('invalid request')




@login_required(login_url=LOGIN_URL)
def reopen(request, task_id):
	if not request.user.is_staff:
		HttpResponse('access denied')

	try:
		task = Task.objects.get(id=task_id)
		issues = task.issues.all()

		for item in issues:
			item.is_open = True
			item.in_progress = True
			item.save()

		task.is_running = True
		task.save()

		return redirect('/task/'+task_id+'/')

	except ObjectDoesNotExist as e:
		pass

	return HttpResponse('invalid request')
