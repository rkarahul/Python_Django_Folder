from django.shortcuts import render

# Create your views here.
def course_django(request):
    return render(request, 'courseone.html')

def course_python(request):
    return render(request, 'coursetwo.html')