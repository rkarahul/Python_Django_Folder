from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    a = '<h1>Hello Chacha</h1>'
    return HttpResponse(a)