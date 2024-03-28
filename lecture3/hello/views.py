from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def mj(request):
    return HttpResponse("Hello, MJ!")

def kite(request):
    return HttpResponse("Hello, Kite!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")