from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request,'fees/feesone.html',{'tittle':'fees Django','cname': 'Django','charge':'300'})

def fees_python(request):
    return render(request,'fees/feestwo.html',{'tittle':'fees python','cname': 'python','charge':'1000'})