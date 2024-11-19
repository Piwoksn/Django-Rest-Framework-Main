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
    path("modify/<int:pk>", views.PostRetrieveUpdateDelete.as_view(), name="modify"),
    path("mixinclass/", views.GetPost_with_Mixins.as_view(), name="mixin" ),
    path("crud/<int:pk>", views.Retrieve_Updat_Delete_with_Mixin.as_view(), name="crud"),
]