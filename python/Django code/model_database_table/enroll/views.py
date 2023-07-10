from django.shortcuts import render
from .models import Student

# Create your views here.

def student(request):
    # stud = Student.objects.get(pk=1)
    stud = Student.objects.all()
    return render(request,'enroll/index.html',{'stu':stud})