from account.models import Account
from django.db import models
from generic.variables import ISSUE_IMAGE_DIR
from uuid import uuid4

TASK_REPORT = (
	('St', 'Satisfied-Service'),
	('Ps', 'Poor-Service'),
	('Ns', 'No-Service')
)


class Issue(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	body = models.TextField()
	in_progress = models.BooleanField(default=False)
	is_open = models.BooleanField(default=True)
	time_date = models.DateTimeField(auto_now=True)
	address = models.CharField(max_length=100)
	media = models.ImageField(upload_to=ISSUE_IMAGE_DIR, blank=True, null=True)
	vote = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title + ' : ' + self.address



class IssueComment(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	body = models.TextField()
	time_date = models.DateTimeField(auto_now=True)


class IssueVote(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)



class Task(models.Model):
	title = models.CharField(max_length=80)
	description = models.TextField()
	time_date = models.DateTimeField(auto_now_add=True)
	is_running = models.BooleanField(default=True)
	issues = models.ManyToManyField(Issue)

	def __str__(self):
		return self.title



class UserTaskReport(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	report = models.CharField(max_length=2, choices=TASK_REPORT)
	time_date = models.DateTimeField(auto_now_add=True)
