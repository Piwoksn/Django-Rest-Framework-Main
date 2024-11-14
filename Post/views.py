# # from django.shortcuts import render
# from django.http import JsonResponse, HttpRequest


# def homepage(request:HttpRequest):
#     response = {
#         "message": "Hello World",
#     }
#     return JsonResponse(data=response)


from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(http_method_names=["GET"])
def homepage(request:Request):
    response = {"message": "Hello World"}
    return Response(data=response, status= status.HTTP_200_OK)