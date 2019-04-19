from api.serializer import IssueSerializer
from api.tokenization import decode as token_decode
from home.models import Issue

from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import NotFound



@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def issue_list(request, many=True):
	token = request.GET.get('token', None)
	locale = request.GET.get('locale', None)
	if token is None:
		raise NotFound('request not found')

	data = token_decode(token)
	if data is None:
		raise NotFound('invalid request')

	user_id = data['user_id']
	if request.user.id != user_id:
		PermissionDenied('access denied')

	if locale is None:
		raise NotFound('request not found')

	result = Issue.objects.all()
	serializer = IssueSerializer(result, many=True)
	return Response(serializer.data)