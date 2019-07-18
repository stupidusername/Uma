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

# URL patters for development environments.
if settings.DEBUG:

    import debug_toolbar
    from django.conf import settings
    from django.conf.urls.static import static

    debug_urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ]
    debug_urlpatterns += \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += debug_urlpatterns
