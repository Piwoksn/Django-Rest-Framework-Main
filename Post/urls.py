from django.urls import path
from . import views

urlpatterns = [
    path("post", views.homepage, name= "postApi/")
]