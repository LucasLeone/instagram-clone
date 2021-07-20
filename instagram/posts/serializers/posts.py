"""Post serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from instagram.posts.models import Post


class PostModelSerializer(serializers.ModelSerializer):
    """Post model serializer."""

    class Meta:
        """Meta class."""

        model = Post
        fields = '__all__'
        read_only_fields = (
            'user',
            'file',
            'text'
        )