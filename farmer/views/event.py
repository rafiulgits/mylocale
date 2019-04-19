from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse

from farmer.models import Event
from farmer.forms import EventForm

from generic.variables import LOGIN_URL

def view(request,uid):
	try:
		event = Event.objects.get(uid=uid)
		context = {}
		context['event'] = event

		return render(request, 'farmer/event/view.html', context)

	except ObjectDoesNotExist as e:
		HttpResponse('Invalid request')




def list(request):
	context = {}
	event_list = Event.objects.all()
	context['event_list'] = event_list

	return render(request, 'farmer/event/list.html', context)



@login_required(login_url=LOGIN_URL)
def create(request):
	if not request.user.is_staff:
		return HttpResponse('access denied')

	if request.method == 'POST':
		form = EventForm(request.POST, user=request.user)
		if form.is_valid():
			event = form.save()
			return redirect('/agriculture/event/'+str(event.uid)+'/')
		else:
			print(form.errors)

	form = EventForm()
	context = {}
	context['form'] = form

	return render(request, 'farmer/event/create.html', context)