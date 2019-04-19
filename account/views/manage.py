from account.forms import ProfileUpdateForm
from account.models import Account

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse

from generic.variables import LOGIN_URL

from home.models import Issue



@login_required(login_url=LOGIN_URL)
def profile(request):
	context = {}
	user = request.user
	issues = Issue.objects.filter(user_id=user.id)
	context['issues'] = issues

	return render(request, 'account/manage/profile.html',context)


@login_required(login_url=LOGIN_URL)
def update(request):
	context = {}
	if request.method == 'POST':
		form = ProfileUpdateForm(request.POST, user=request.user)
		if form.is_valid():
			request.user.name = form.cleaned_data['name']
			request.user.email = form.cleaned_data['email']
			request.user.gender = form.cleaned_data['gender']
			request.user.save()

			return redirect('/account/')

	form = ProfileUpdateForm(user=request.user)

	context['form'] = form

	return render(request, 'account/manage/update.html', context)
