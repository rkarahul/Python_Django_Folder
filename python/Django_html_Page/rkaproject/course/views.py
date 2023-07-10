from django.shortcuts import render

# Create your views here.
def course_django(request):
    return render(request,'course/courseone.html',{'tittle':'course Django','cname': 'C_Django'})

def course_python(request):
    return render(request,'course/coursetwo.html',{'tittle':'fees python','cname': 'C_python'})