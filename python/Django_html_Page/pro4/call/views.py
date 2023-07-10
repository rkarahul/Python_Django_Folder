from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def call(request):
    return HttpResponse ('<h1>Ka haal Ba chacha</h1>')