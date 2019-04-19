from django.urls import path


from home.views import manage, issue, task, staff

urlpatterns = [

	path('', manage.index, name='index'),

	path('search/', manage.search, name='search'),

	path('staff-panel/', staff.panel, name='staff-panel'),
	path('staff-panel/opened-tasklist/', staff.open_tasklist, name='open_tasklist'),
	path('staff-panel/closed-tasklist/', staff.close_tasklist, name='close_tasklist'),
	path('staff-panel/open-issuelist/', staff.open_issuelist, name='open_issuelist'),
	path('staff-panel/progress-issuelist/', staff.progress_issuelist, name='progress_issuelist'),
	path('staff-panel/close-issuelist/', staff.close_issuelist, name='close_issuelist'),

	path('issue/create/', issue.create, name='issue-create'),
	path('issue/list/', issue.list, name='issue-list'),
	path('issue/view/', issue.view, name='issue-view'),


	path('task/create/', task.create, name='task-create'),
	path('task/list/', task.list, name='task-list'),
	path('task/view/', task.view, name='task-view'),
]