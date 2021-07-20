"""Profile model."""

# Django
from django.db import models
# from django.contrib.auth import get_user_model

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
        return self.user.username



# FOLLOW SYSTEM

# UserModel = get_user_model()

# class UserFollowing(InstagramModel):
#     """Follower system."""

#     user_id = models.ForeignKey(UserModel, related_name='following', on_delete=models.CASCADE)
#     following_user_id = models.ForeignKey(UserModel, related_name='followers', on_delete=models.CASCADE)

#     class Meta:
#         """Meta class."""

#         constraints = [
#             models.UniqueConstraint(fields=['user_id', 'following_user_id'], name='unique_followers')
#         ]

#     def __str__(self):
#         """Return user follow other user."""
#         return f'{self.user_id} follows {self.following_user_id}'
