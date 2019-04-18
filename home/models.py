from account.models import Account
from django.db import models
from generic.variables import ISSUE_IMAGE_DIR
from uuid import uuid4

ISSUE_REPORT = (
	('St', 'Satisfied-Service'),
	('Ps', 'Poor-Service'),
	('Ns', 'No-Service')
)


class Location(model.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	geo_lat = models.DecimalField(max_digits=22, decimal_places=16)
	geo_lng = models.DecimalField(max_digits=22, decimal_places=16)
	address = models.CharField(max_length=100)


class Issue(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	body = models.TextField()
	location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True)
	is_open = models.BooleanField(default=True)
	time_date = models.DateTimeField(auto_now=True)
	media = models.ImageField(upload_to=ISSUE_IMAGE_DIR, blank=True, null=True)
	total_st = models.PositiveIntegerField(default=0)
	total_ps = models.PositiveIntegerField(default=0)
	total_ns = models.PositiveIntegerField(default=0)



class IssueComment(models.Model):
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	body = models.TextField()
	time_date = models.DateTimeField(auto_now=True)



class UserIssueReport(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
	report = models.CharField(choices=ISSUE_REPORT)
	time_date = models.DateTimeField(auto_now=True)
