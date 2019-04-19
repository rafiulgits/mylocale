from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, Http404

from farmer.models import Event

from generic.variables import LOGIN_URL

def view(request, uid):
	try:
		event = Event.objects.get(uid=uid)
		context = {}
		context['event'] = event

		return render(request, 'farmer/event/view.html', context)

	except ObjectDoesNotExist as e:
		Http404('Invalid request')




def list(request):
	context = {}
	event_list = Event.objects.all()
	context['event_list'] = event_list

	return render(request, 'farmer/event/list.html', context)



@login_required(login_url=LOGIN_URL)
def create(request):
	if not request.user.is_staff:
		return Http404('access denied')

	form = EventForm()
	context = {}
	context['form'] = form

	return render(request, 'farmer/event/create.html', context)