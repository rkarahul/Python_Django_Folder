from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fees_django(request):
    # return HttpResponse('<h1>300</h1>')
    return render(request,'nested_table.html')

def fees_python(request):
    # return HttpResponse('<h1>500</h1>')
    return render(request,'form2.html')