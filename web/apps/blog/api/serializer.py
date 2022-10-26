from rest_framework import serializers
from apps.blog.models import Post, Category
from django.db import transaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title"]


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "content",
            "author",
            "category",
        ]

    def create(self, validated_data):
        categories = validated_data.pop("category")
        post = Post.objects.create(**validated_data)
        for category in categories:
            c = Category.objects.create(**category)
            c.post.add(post)
        return post
