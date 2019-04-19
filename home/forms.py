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


class IssueUpdateForm(forms.ModelForm):

	class Meta:
		model = Issue
		fields = ['title', 'body', 'address']

		widgets = {
			'title' : forms.TextInput(attrs=
				{'class' : 'form-control', 'placeholder' : 'Broken Roard'}),
			'body' : forms.Textarea(attrs=
				{'class' : 'form-control', 'placeholder' : 'Issue Description'}),
			'address' : forms.TextInput(attrs=
				{'class' : 'form-control'})
		}


	def __init__(self, *args,**kwargs):
		self.issue = kwargs.pop('issue', None)
		super(IssueUpdateForm, self).__init__(*args, **kwargs)
		if self.issue:
			self.fields['title'].initial = self.issue.title
			self.fields['body'].initial = self.issue.body
			self.fields['address'].initial = self.issue.address





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
			comment.save()

		return comment


	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		self.issue = kwargs.pop('issue', None)
		super(IssueCommentForm, self).__init__(*args, **kwargs)




class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ['title','description', 'issues']


	def save(self, commit=True):
		task = super(TaskForm, self).save(commit=True)

		issues = self.cleaned_data['issues']
		for item in list(issues):
			task.issues.add(item)
			item.in_progress = True
			item.save()

		if commit:
			task.save()
		return task



	def __init__(self, *args, **kwargs):
		super(TaskForm, self).__init__(*args, **kwargs)

		self.fields['title'].widget = forms.TextInput(attrs=
				{'class' : 'form-control', 'placeholder' : 'What is your task?'})

		self.fields['description'].widget = forms.Textarea(attrs=
				{'class' : 'form-control', 
				'placeholder' : 'Define your task'})

		self.fields['issues'].widget = forms.CheckboxSelectMultiple(attrs={})

		self.fields['issues'].queryset = Issue.objects.filter(is_open=True).filter(in_progress=False)



class TaskUpdateForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ['title','description']


	def __init__(self, *args, **kwargs):
		self.task = kwargs.pop('task', None)
		super(TaskUpdateForm, self).__init__(*args, **kwargs)

		self.fields['title'].widget = forms.TextInput(attrs=
				{'class' : 'form-control', 'placeholder' : 'What is your task?'})
		self.fields['title'].initial = self.task.title

		self.fields['description'].widget = forms.Textarea(attrs=
				{'class' : 'form-control', 
				'placeholder' : 'Define your task'})
		self.fields['description'].initial = self.task.description




class UserTaskReportForm(forms.ModelForm):
	class Meta:
		model = UserTaskReport
		fields = ['report']
		widgets = {
			'report' : forms.Select(attrs=
				{'class' : 'custom-select'})
		}


	def __init__(self, *args, **kwargs):
		self.user_report = kwargs.pop('report_obj', None)
		super(UserTaskReportForm, self).__init__(*args, **kwargs)

		if self.user_report is not None:
			self.fields['report'].initial = self.user_report.report
