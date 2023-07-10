from django.shortcuts import render

# Create your views here.
def website(rka):
    return render(rka,'website/index.html')
