from django import forms

from home.models import Issue, IssueComment, UserIssueReport


class IssueForm(forms.ModelForm):
	class Meta:
		model = Issue





class IssueCommentForm(forms.ModelForm):
	class Meta:
		model = IssueComment





class UserIssueReportForm(forms.ModelForm):
	class Meta:
		model = UserIssueReport