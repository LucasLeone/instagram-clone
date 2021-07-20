"""Posts views."""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework import permissions

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from instagram.posts.serializers.posts import PostModelSerializer

# Models
from instagram.posts.models import Post


class PostViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """Post view set."""

    serializer_class = PostModelSerializer
    # lookup_field = 'user'

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Post.objects.all()
        if self.action == 'list':
            return queryset.filter(is_active=True)
        return queryset

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]
