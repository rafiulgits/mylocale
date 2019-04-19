from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, Http404

from farmer.models import Crop
from farmer.forms import CropForm

from generic.variables import LOGIN_URL

def view(request):
	try:
		# crop = Crop.objects.get(uid=uid)
		context = {}
		# context['crop'] = crop

		return render(request, 'farmer/crop/view.html', context)

	except ObjectDoesNotExist as e:
		Http404('Invalid request')




def list(request):
	context = {}
	crop_list = Crop.objects.all()
	context['crop_list'] = crop_list

	return render(request, 'farmer/crop/list.html', context)



@login_required(login_url=LOGIN_URL)
def create(request):
	if not request.user.is_staff:
		return Http404('access denied')

	if request.method == 'POST':
		form = CropForm(request.POST, request.FILES)
		if form.is_valid():
			crop = Crop(user=request.user)
			crop.category = form.cleaned_data['category']
			crop.name = form.cleaned_data['name']
			crop.description = form.cleaned_data['description']
			crop.media = form.cleaned_data['media']

			crop.save()

			return redirect('/agriculture/crop/'+str(crop.uid)+'/')
		else:
			print('form is not valid')
			print(form.errors)


	form = CropForm()
	context = {}
	context['form'] = form

	return render(request, 'farmer/crop/create.html', context)