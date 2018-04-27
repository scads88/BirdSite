from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2> Andrew Service Offered </h2>")
# Create your views here.
