from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>This is App1 first view</h1>')
def second(request):
    return HttpResponse('<h2>This is Second view</h2>')