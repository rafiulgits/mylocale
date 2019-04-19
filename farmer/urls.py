from django.urls import path

from farmer.views import crop, event, index


urlpatterns = [
	
	path('', index.index, name='index'),
	
	path('crop/all/', crop.list, name='crop-list'),
	path('crop/create/', crop.create, name='crop-create'),
	path('crop/<uid>/', crop.view, name='crop-view'),

	path('event/all/', event.list, name='event-list'),
	path('event/create/', event.create, name='event-create'),
	path('event/<uid>/', event.view, name='event-view'),
]