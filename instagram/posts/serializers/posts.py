"""Post serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from instagram.posts.models import Post


class PostModelSerializer(serializers.ModelSerializer):
    """Post model serializer."""

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        """Meta class."""

        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.Serializer):
    """Post create serializer.
    
    Handle create data validation.
    """

    file = serializers.FileField()
    text = serializers.CharField(max_length=500, allow_blank=True)
    is_active = serializers.BooleanField(required=True)

    def create(self, data):
        """Handle post creation."""
        post = Post.objects.create(**data)
        return post