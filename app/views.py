from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.

def hello_world(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World!")