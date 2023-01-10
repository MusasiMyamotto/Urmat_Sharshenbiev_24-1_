from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.

def hello(request):
    if request.method == 'GET':
        return HttpResponse('hello! its my project')

def now_date(request):
    now = datetime.now()
    if request.method == 'GET':
        return HttpResponse(f'The current date is {now}')

def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user')