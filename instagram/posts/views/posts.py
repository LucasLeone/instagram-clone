"""Posts views."""

# Django REST Framework
from rest_framework import generics
from rest_framework.decorators import action

# Permissions
from instagram.posts.permissions import IsPostOwner
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Serializers
from instagram.posts.serializers.posts import (
    PostModelSerializer,
)

# Models
from instagram.posts.models import Post


class PostList(generics.ListCreateAPIView):
    """List and Create posts."""

    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Create post."""
        serializer.save(user=self.request.user)


class PostDetail(generics.RetrieveDestroyAPIView):
    """Detail, Update and Delete post."""

    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsPostOwner]