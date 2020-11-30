"""HabitatYConstruccion URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
                  path('api/', include(('Facebook_API.urls', 'api'), namespace='api')),
                  path('social-auth/', include('social_django.urls', namespace='social'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
