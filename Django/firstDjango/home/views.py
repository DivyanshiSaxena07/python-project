from django.shortcuts import render,HttpResponse


def index(request):
    return HttpResponse("Hello world!")


def about(request):
    return HttpResponse("This is about page")
# Create your views here.
