from django import forms

from home.models import Issue, IssueComment, Task, UserTaskReport


class IssueForm(forms.ModelForm):

	class Meta:
		model = Issue
		fields = ['title', 'body', 'media', 'address']

		widgets = {
			'title' : forms.TextInput(attrs=
				{'class' : 'form-control', 'placeholder' : 'Broken Roard'}),
			'body' : forms.Textarea(attrs=
				{'class' : 'form-control', 'placeholder' : 'Issue Description'}),
			'media' : forms.FileInput(attrs=
				{'class' : 'form-control'}),
			'address' : forms.TextInput(attrs=
				{'class' : 'form-control'})
		}


	def save(self, commit=True):
		issue = super(IssueForm, self).save(commit=False)
		issue.user = self.user
		if commit:
			issue.save()

		return issue


	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(IssueForm, self).__init__(*args, **kwargs)



class IssueCommentForm(forms.ModelForm):
	class Meta:
		model = IssueComment
		fields = ['body']

		widgets = {
			'body' : forms.Textarea(attrs=
				{'class' : 'form-control', 'placeholder' : 'Issue Description'})
		}


	def save(self, commit=True):
		comment = super(IssueCommentForm, self).save(commit=False)
		comment.user = self.user
		comment.issue = self.issue
		if commit:
			issue.save()

		return issue


	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		self.issue = kwargs.pop('issue', None)
		super(IssueCommentForm, self).__init__(*args, **kwargs)




class TaskForm(forms.ModelForm):
	issues = forms.ModelMultipleChoiceField(queryset=Issue.objects.all())

	class Meta:
		model = Task
		fields = ['title','description']

		widgets = {
			'title' : forms.TextInput(attrs=
				{'class' : 'form-control', 'placeholder' : 'What is your task?'}),
			'description' : forms.Textarea(attrs=
				{'class' : 'form-control', 
				'placeholder' : 'Define your task'})
		}



	def save(self, commit=True):
		task = super(TaskForm, self).save(commit=False)
		if commit:
			task.save()
		return task




class UserTaskReportForm(forms.ModelForm):
	class Meta:
		model = UserTaskReport
		fields = ['report']
		widgets = {
			'report' : forms.Select(attrs=
				{'class' : 'custom-select'})
		}


	def save(self, commit=True):
		report = super(UserIssueReportForm, self).save(commit=False)
		report.user = self.user
		report.task = self.task

		if commit:
			report.save()
		return report


	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		self.task = kwargs.pop('task', None)
		super(UserIssueReportForm, self).__init__(*args, **kwargs)
