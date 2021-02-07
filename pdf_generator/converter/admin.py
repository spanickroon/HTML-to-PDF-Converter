from django.contrib import admin
from .models import LinkInternetResource, ProcessingRequest, Recipient

admin.site.register(LinkInternetResource)
admin.site.register(ProcessingRequest)
admin.site.register(Recipient)
