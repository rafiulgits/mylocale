from django.shortcuts import render, redirect, HttpResponse


def index(request):
	context = {}
	return render(request, 'farmer/index.html', context)