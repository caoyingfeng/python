from django.http import HttpResponse
from django.shortcuts import redirect


def index(response):
    return HttpResponse('index')


def login(response):
    return redirect('/index')
