from django.shortcuts import render, redirect, HttpResponse


def index(request):
	context = {}

	return render(request, 'home/manage/index.html', context)