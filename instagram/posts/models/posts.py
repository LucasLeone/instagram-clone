"""Post model."""

# Django
from django.db import models

# Utils
from instagram.utils.models import InstagramModel


class Post(InstagramModel):
    """Post model."""

    file = models.FileField(upload_to='files', null=True, blank=True)

    text = models.TextField(max_length=500)