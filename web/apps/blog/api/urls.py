from django.urls import path

from .views import PostListCreateAPIView, CategoryListAPIView

urlpatterns = [
    path("posts/", PostListCreateAPIView.as_view()),
    path("categories/", CategoryListAPIView.as_view()),
]
