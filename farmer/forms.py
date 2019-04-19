from django import forms
from farmer.models import Crop, Event


class CropForm(forms.ModelForm):
	class Meta:
		model = Crop
		fields = ['category', 'name', 'description', 'media',]

		widgets = {
			'category':forms.Select(attrs=
				{'class' : 'custom-select'}),

			'name':forms.TextInput(attrs=
				{'class':'form-control',
				'placeholder' : 'Mango'}),
			'description':forms.Textarea(attrs=
				{'class':'form-control', 
				'placeholder': 'Description about mango'}),
		}




class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = [ 'title', 'description', 'time', 'date', 'address',]

		widgets = {

			'title':forms.TextInput(attrs=
				{'class':'form-control',
				'placeholder' : 'সরকারীভাবে বীজ বিরতরণ'}),
			'description':forms.Textarea(attrs=
				{'class':'form-control', 
				'placeholder': 'Description'}),
			'time' : forms.TimeInput(attrs={'type':'time'}),
			'date' : forms.DateInput(attrs={'type': 'date'}),

			'address':forms.TextInput(attrs=
				{'class':'form-control',
				'placeholder' : 'Event Location Address'})
		}


	def save(self, commit=True):
		event = super(EventForm, self).save(commit=False)
		event.user = self.user
		if commit:
			event.save()

		return event



	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(EventForm, self).__init__(*args, **kwargs)
