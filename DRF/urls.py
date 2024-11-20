
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Post.views import Using_Viewsets, Model_viewset


router = DefaultRouter()
router2 = DefaultRouter()


router.register("", Using_Viewsets, basename="viewsets_api")

router2.register("", Model_viewset, basename="model_viewset")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("post/", include("Post.urls")),
    path("viewsets_api/", include(router.urls)),
    path("model_viewset/", include(router2.urls)),
]
