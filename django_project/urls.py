from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("pages.urls")),
    path("aws/", include("exposing_aws.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
