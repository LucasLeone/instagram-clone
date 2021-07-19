"""Profile model."""

# Django
from django.db import models

# Utilities
from instagram.utils.models import InstagramModel


class Profile(InstagramModel):
    """Profile model.
    
    A profile holds a user's public data like biography, picture
    and followings.
    THE FOLLOWER SYSTEM IS THE NEXT STEP.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)

    def __str__(self):
        """Return user profile"""
        return self.user