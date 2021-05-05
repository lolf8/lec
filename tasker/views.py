from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def tasks(request):
    return render(request,'tasker/hi.html')

def greet(request,name):
    return render(request,'tasker/hi.html',{
        "name":name.capitalize()
    })

def show(request):
    now = datetime.datetime.now()
    return render(request,'tasker/time.html',{
        'time': now.strftime("%H:%M:%S %Y/%m/%d")
    })
