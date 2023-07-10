from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def learn_django(rka):
    return HttpResponse('<h1>Mission Successfull</h1>')