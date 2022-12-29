from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def praveen(request):
    return HttpResponse('<h1>Praveen</h1>')

def sonu(request):
    return HttpResponse('<h2>Sonu</h2>')