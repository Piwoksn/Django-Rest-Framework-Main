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
from .models import Post
from .serializers import Modelserializer
from django.shortcuts import get_object_or_404

posts = [
    {
        "id": 1,
        "title": "Why is my name Noble Piwoks",
        "content": "Discovering yourself"
    },
    {
        "id": 2,
        "title": "How is Life so far?",
        "content": "In Gods Hands"
    },
    {
        "id": 3,
        "title": "What are your achievements",
        "content": "Find out for yourself"
    }
]


@api_view(http_method_names=["GET", "POST"])
def homepage(request:Request):
    
    if request.method == 'POST':
        data = request.data
        response = response = [{"message": "Hello World"},
                {"name": "Piwoks Noble"}, data]
        return Response(data= response, status=status.HTTP_201_CREATED) 
       
    response = [{"message": "Hello World"},
                {"name": "Piwoks Noble"}]
    return Response(data=response, status= status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def list_post(request:Request):
    return Response(data=posts, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail(request:Request, pk:int):
    post = get_object_or_404(Post, pk=pk)
    # if post:
    #     return Response(data=post, status=status.HTTP_200_OK)
    serialize = Modelserializer(instance=post)
    response={"message":"Found", "data":serialize.data}
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET", "POST"])
def model(request:Request):
    posts= Post.objects.all()
    serializer = Modelserializer(instance=posts, many=True)
    
    if request.method == 'POST':
        data = request.data
        
        serializer = Modelserializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            response = {
            "message":"Created",
            "data": data
            }
            
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    response = {
        "message": "post",
        "data": serializer.data
    }
    return Response(data=response, status=status.HTTP_200_OK)
