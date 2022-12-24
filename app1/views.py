from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def shambhavi(request):
    return HttpResponse('<h1><marquee> shambhavi is very talented girl<h1><marquee>')
def vani(request):
    return HttpResponse('<h1><marquee> vani is very pretty</h1></marquee>')