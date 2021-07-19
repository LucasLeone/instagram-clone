"""Post model."""

# Django
from django.db import models

# Utils
from instagram.utils.models import InstagramModel


class Post(InstagramModel):
    """Post model.
    
    THE FAVS SYSTEM IS THE NEXT STEP.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    file = models.FileField(upload_to='posts/files/')

    text = models.TextField(max_length=500)

    def __str__(self):
        """Return post user."""
        return self.user