from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"hello/index.html")


def amaan(request):
    return HttpResponse("Hello, Amaan")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request,name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    
    return render(request,"hello/greet.html", {
        "name":name.capitalize()
        })