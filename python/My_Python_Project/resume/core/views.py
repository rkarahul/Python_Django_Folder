from django.shortcuts import render
from .models import resume

# Create your views here.
def home(request):
    context = {'home': 'active'}
    return render(request,'core/home.html', context)

def contact(request):
    context = {'contact': 'active'}
    # name = request.POST["inputName"]
    # email = request.POST["inputEmail"]
    # subject = request.POST["inputSubject"]
    # message = request.POST["inputMessage"]
    # resume_info = resume_info(name=name,email=email,subject=subject,message=message)
    # resume_info.save()
    return render(request,'core/contact.html', context)
