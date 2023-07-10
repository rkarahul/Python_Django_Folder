from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def fees_django(rka):
    return HttpResponse('Ka Haal Ba Bhai')

def course_django(request):
    return HttpResponse('Thik ba Bhai')