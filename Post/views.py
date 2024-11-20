# # from django.shortcuts import render
# from django.http import JsonResponse, HttpRequest


# def homepage(request:HttpRequest):
#     response = {
#         "message": "Hello World",
#     }
#     return JsonResponse(data=response)


from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view, APIView
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


@api_view(http_method_names=["PUT"])
def updatedata(request:Request, pk:int):
    db = get_object_or_404(Post, pk=pk)
    data = request.data
    serialize = Modelserializer(instance=db, data=data)
    if serialize.is_valid():
        serialize.save()
        response = {
            "message": "Updated Successfully",
            "data": serialize.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"])
def deletepost(request:Request, pk):
    db = get_object_or_404(Post, pk=pk)
    db.delete()
    response = {
        "message": f"Deleted id = {pk}"
    }
    return Response(data=response, status=status.HTTP_200_OK)


class PostGetClassView(APIView):
    serializer = Modelserializer
    
    def get(self, request:Request, *args, **kwargs):
        db = Post.objects.all()
        
        serialized = self.serializer(instance=db, many=True)
        response = {
            "message": "database",
            "data": serialized.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    def post(self, request:Request, *args, **kwargs):
        data = request.data
        serialized = self.serializer(data=data)
        
        if serialized.is_valid():
            serialized.save()
            response = {
                "message": "Created Successfully"
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serialized.errors, status=status.HTTP_400_BAD_REQUEST)

class PostRetrieveUpdateDelete(APIView):
    serializer = Modelserializer
    
    def get(self, request:Request, pk:int, *args, **kwargs):
        item = get_object_or_404(Post, pk=pk)
        serialized = self.serializer(instance = item)
        
        response = {
            "message": "Single Item",
            "data": serialized.data
        }
        
        return Response(data=response, status=status.HTTP_200_OK)
    
    def put(self, request:Request, pk:int):
        data = request.data
        item = get_object_or_404(Post, pk=pk)
        serialized = self.serializer(instance = item, data=data)
        if serialized.is_valid():
            serialized.save()
            
            response = {
                "message": f"id = {pk} Updated Successfully",
                "data": serialized.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request:Request, pk):
        item = get_object_or_404(Post, pk=pk)
        item.delete()
        response = {
            "message": f"Deleted Successfully -  id = {pk}",
        }
        
        return Response(data=response, status=status.HTTP_200_OK)


class GetPost_with_Mixins(generics.GenericAPIView, 
                          mixins.ListModelMixin, 
                          mixins.CreateModelMixin):
    serializer_class = Modelserializer
    queryset = Post.objects.all()
    
    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Retrieve_Updat_Delete_with_Mixin(generics.GenericAPIView,
                                       mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin):
    serializer_class = Modelserializer
    queryset = Post.objects.all()
    
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class Using_Viewsets(viewsets.ViewSet):
    def list(self, request:Request):
        queryset = Post.objects.all()
        serializer = Modelserializer(instance= queryset, many=True)
        return Response(data=serializer.data, status= status.HTTP_200_OK)
    
    def retrieve(self, request:Request, pk):
        item = get_object_or_404(Post, pk=pk)
        
        serializer = Modelserializer(instance = item)
        return Response(data=serializer.data, status = status.HTTP_200_OK)