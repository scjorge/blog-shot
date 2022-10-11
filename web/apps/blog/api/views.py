from rest_framework.generics import ListCreateAPIView, ListAPIView

from apps.blog.models import Post, Category
from apps.blog.api.serializer import PostSerializer, CategorySerializer


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
