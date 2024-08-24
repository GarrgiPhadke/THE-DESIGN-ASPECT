from django.shortcuts import render

def myservice(request):
    return render(request, 'myservice.html')

# Create your views here.
