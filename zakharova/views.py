from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('This is information about the project')

def home(request):
    return render(request,'home.html', {'greeting':'Good day!'})