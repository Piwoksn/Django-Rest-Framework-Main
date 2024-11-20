
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Post.views import Using_Viewsets


router = DefaultRouter()

router.register("", Using_Viewsets, basename="viewsets_api")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("post/", include("Post.urls")),
    path("viewsets_api/", include(router.urls))
]
