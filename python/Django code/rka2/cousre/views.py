from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Home Page')


def learn_django(request):
    return HttpResponse('Hello Rahul')

def learn_python(rka):
    return HttpResponse('<h1>Hello Python</h1>')

def learn_var(rka):
    a = '<h1>Hello Variable</h1>'
    return HttpResponse(a)

def learn_math(request):
    a = 10 + 10
    return HttpResponse(a)

def learn_format(request):
    a = '<h1>Rahul Bhai</h1>'
    return HttpResponse(f'Hello How are You {a}')