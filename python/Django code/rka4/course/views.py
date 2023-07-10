from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def fees_django(rka):
    return HttpResponse('Kaha ho')

def course_django(request):
    return HttpResponse('siwan')