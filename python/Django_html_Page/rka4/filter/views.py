from django.shortcuts import render

# Create your views here.
def filter(request):
    cname = 'Django'
    duration = '4 month'
    seats = 10
    django_details = {'cn':cname, 'du':duration, 'st':seats}
    # django_details = {'nm':'django is awesome'}
    # return render(request, 'filter/index.html',django_details)
    return render(request, 'filter/index.html',context = django_details)