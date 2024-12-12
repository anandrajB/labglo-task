from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from accounts.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("app/", include("accounts.urls")),
    path("docs/", include("myproject.urls.docs")),
]
