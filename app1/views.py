from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_app1_first(request):
    return HttpResponse('<h1>I am a Good boy</h1>')

def my_app1_second(request):
    return HttpResponse('<h1><marquee> I am a Good boy</marquee></h1>')
