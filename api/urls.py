from api.views import issue_list

from django.urls import path

urlpatterns = [

	path('locale-issues/', issue_list, name='issue_list'),
]