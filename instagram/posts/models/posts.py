"""Post model."""

# Django
from django.db import models

# Utils
from instagram.utils.models import InstagramModel


class Post(InstagramModel):
    """Post model.
    
    THE FAVS SYSTEM IS THE NEXT STEP.
    """

    user = models.ForeignKey('users.User',related_name='posts', on_delete=models.CASCADE)

    file = models.FileField(upload_to='posts/files/')

    text = models.TextField(max_length=500, blank=True)

    is_active = models.BooleanField(
        'is active post',
        default=True,
        blank=False
    )

    def __str__(self):
        """Return post user."""
        return self.user.username