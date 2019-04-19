from api.tokenization import encode as token_encode

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse

from generic.variables import LOGIN_URL

from home.models import Issue, IssueComment, IssueVote
from home.forms import IssueForm, IssueCommentForm, IssueUpdateForm


def view(request, uid):
	try:
		context = {}
		issue = Issue.objects.get(uid=uid)
		if request.user.is_authenticated:

			if request.method == 'POST':
				form = IssueCommentForm(request.POST, issue=issue, user=request.user)
				if form.is_valid():
					form.save()
					return redirect('/issue/'+uid+'/#form-block')
			form = IssueCommentForm()
			context['form'] = form

			user_vote = IssueVote.objects.filter(issue_id=issue.uid, user_id=request.user.id).first()
			if user_vote:
				context['has_vote'] = True
			else:
				context['has_vote'] = False


			if request.user != issue.user:
				vote = request.GET.get('vote', None)
				unvote = request.GET.get('unvote', None)
				if vote:
					if user_vote is None:
						IssueVote.objects.create(user=request.user, issue=issue)
						issue.vote += 1
						issue.save()

					context['has_vote'] = True


				elif unvote:
					if user_vote:
						user_vote.delete()
						issue.vote -= 1
						issue.save()

					context['has_vote'] = False

		comments = IssueComment.objects.filter(issue_id=uid).order_by('-time_date')

		context['issue'] = issue
		context['comments'] = comments

		return render(request, 'home/issue/view.html', context)

	except ObjectDoesNotExist as e:
		return HttpResponse('invalid request')



@login_required(login_url=LOGIN_URL)
def create(request):
	if request.user.is_staff:
		return HttpResponse('You are not allowed to create issue')


	if request.method == 'POST':
		form = IssueForm(request.POST, request.FILES, user=request.user)
		if form.is_valid():
			issue = form.save()
			return redirect('/issue/'+str(issue.uid)+'/')

		else:
			print(form.errors)

	token = token_encode({'user_id' : request.user.id })
	context = {}
	context['token'] = token
	

	form = IssueForm()
	context['form'] = form

	return render(request, 'home/issue/create.html', context)



def list(request):
	context = {}
	issue_list = Issue.objects.all()
	context['issue_list'] = issue_list

	return render(request, 'home/issue/list.html', context)


@login_required(login_url=LOGIN_URL)
def delete(request, uid):
	try:
		issue = Issue.objects.get(uid=uid)
		if request.user == issue.user:
			comments = IssueComment.objects.filter(issue_id=issue.uid)
			comments.delete()

			votes = IssueVote.objects.filter(issue_id=issue.uid)
			votes.delete()

			issue.delete()

			return redirect('/issue/list/')
	except ObjectDoesNotExist as e:
		pass

	return HttpResponse('invalid request')



@login_required(login_url=LOGIN_URL)
def update(request, uid):
	try:
		issue = Issue.objects.get(uid=uid)
		if issue.user == request.user:
			context = {}
			if request.method == 'POST':
				form = IssueUpdateForm(request.POST)
				if form.is_valid():
					issue.title = form.cleaned_data['title']
					issue.body = form.cleaned_data['body']
					issue.address = form.cleaned_data['address']

					issue.save()

					return redirect('/issue/'+uid+'/')

				else:
					print(form.errors)


			form = IssueUpdateForm(issue=issue)
			context['form'] = form

			return render(request, 'home/issue/update.html', context)

	except ObjectDoesNotExist as e:
		pass


	return HttpResponse('invalid request')

