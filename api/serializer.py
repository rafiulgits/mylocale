from rest_framework.serializers import ModelSerializer,ReadOnlyField

from home.models import Issue


class IssueSerializer(ModelSerializer):
	user = ReadOnlyField(source='user.name')
	class Meta:
		model = Issue
		fields = ['uid', 'title', 'body', 'address', 'time_date', 'user']