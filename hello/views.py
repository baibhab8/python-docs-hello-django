from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello Baibhab,Good morning! , We are learning Azure and we are happy")
