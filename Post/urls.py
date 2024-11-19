from django.urls import path
from . import views



urlpatterns = [
    path("home/", views.homepage, name= "homepage"),
    path("", views.list_post, name= "list_post"),
    path("<int:pk>", views.post_detail, name="post_detail"),
    path("update/<int:pk>", views.updatedata, name="updatedata"),
    path("delete/<int:pk>", views.deletepost, name="deletepost"),
    path("model/", views.model, name="post_model"),
    path("getPost/", views.PostGetClassView.as_view(), name="getPost"),
]