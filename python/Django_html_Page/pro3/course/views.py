from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return render(request,'course/courseone.html')

def learn_Python(request):
    return render(request,'course/coursetwo.html')