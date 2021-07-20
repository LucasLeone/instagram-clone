"""Posts admin."""

# Django
from django.contrib import admin

# Models
from instagram.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post model admin."""

    list_display = ('user', 'created')
    search_fields = ('user',)