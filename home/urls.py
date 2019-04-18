from django.urls import path


from home.views import manage

urlpatterns = [

	path('', manage.index, name='index'),

]