from django.shortcuts import render
from django.http import JsonResponse, HttpRequest

# Create your views here.

def homepage(request:HttpRequest):
    response = {
        "message": "Hello World",
    }
    return JsonResponse(data=response)