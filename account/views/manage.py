from account.forms import ProfileUpdateForm
from account.models import Account

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse

from generic.variables import LOGIN_URL



@login_required(login_url=LOGIN_URL)
def profile(request):
	context = {}
	user = request.user

	return render(request, 'account/profile/view.html',context)


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

	return render(request, 'account/profile/update.html', context)

