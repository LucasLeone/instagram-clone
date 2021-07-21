"""Posts URLs."""

# Django
from django.urls import include, path

# Views
from .views import posts as post_views


urlpatterns = [
    path('posts/', post_views.PostList.as_view()),
    path('posts/<int:pk>/', post_views.PostDetail.as_view()),
]