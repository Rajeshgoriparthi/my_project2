from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_app2_first(request):
    return HttpResponse('<h1>I am a Bad boy</h1>')


def my_app2_second(request):
    return HttpResponse('<h1><marquee>I am a Bad boy</marquee></h1>')