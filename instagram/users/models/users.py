"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from instagram.utils.models import InstagramModel


class User(InstagramModel, AbstractUser):
    """User model.
    
    Extend from Django's Abstract User.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return first name."""
        return self.first_name