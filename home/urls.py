from django.urls import path


from home.views import manage, issue, task

urlpatterns = [

	path('', manage.index, name='index'),

	path('issue/create/', issue.create, name='issue-create'),
	path('issue/list/', issue.list, name='issue-list'),
	path('issue/<uid>/', issue.view, name='issue-view'),


	path('task/create/', task.create, name='task-create'),
	path('task/list/', task.list, name='task-list'),
	path('task/<task_id>/', task.view, name='task-view'),

]