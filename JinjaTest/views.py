from django.shortcuts import render


def index(request):
    return render(request, "JinjaTest/home.html")
# Create your views here.
