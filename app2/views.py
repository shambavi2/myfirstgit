from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sai(request):
    return HttpResponse('<h1><marquee>sai is looking gorgeous<h1><marquee>')
def mammu(request):
    return HttpResponse('<h1><marquee> mammu eats chocolates daily</h1></marquee>')