"""
Project URL configuration.
"""

from baton.autodiscover import admin
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
]

# Add the Debug Toolbar’s URLs.
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls))
        ] + urlpatterns
