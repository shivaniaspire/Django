from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
	return HttpResponse('<em>My Second app</em>')