from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    return render(request, "hello.html")


def greet(request):
    return render(request, "welcome.html")


def status(request):
    return render(request, "status.html")
