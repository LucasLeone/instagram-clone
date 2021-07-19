"""Main URLs module."""

from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls.conf import include

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    path('', include(('instagram.users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
