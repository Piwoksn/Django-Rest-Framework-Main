# from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from rest_framework import response, request


def homepage(request:HttpRequest):
    response = {
        "message": "Hello World",
    }
    return JsonResponse(data=response)

