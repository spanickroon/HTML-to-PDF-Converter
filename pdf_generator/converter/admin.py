"""A module that binds models to the django admin panel."""

from django.contrib import admin
from .models import LinkInternetResource, ProcessingRequest

admin.site.register(LinkInternetResource)
admin.site.register(ProcessingRequest)
