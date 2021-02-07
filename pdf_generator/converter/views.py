"""Application views module."""

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.renderers import TemplateHTMLRenderer

from django.http import HttpResponse
from .serializers import ContentUploadSerializer
from .services.distribution_entered_data import DistributionEnteredData
from .services.converter import Converter


class ContentUploadViewSet(ViewSet):
    """Main view that is responsible for get and post requests."""

    serializer_class = ContentUploadSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'converting_data.html'

    def create(self, request: Request) -> HttpResponse:
        """The method that is triggered on post request."""

        file_upload = request.data.get('file_upload')
        url_upload = request.data.get('url_upload')
        email_upload = request.data.get('email_upload')

        return DistributionEnteredData.procesing_request_by_data_priority(
            file_upload,
            url_upload,
            email_upload
        )

    def retrieve(self, request: Request) -> Response:
        """The method that is triggered on get request."""

        return Response({'serializer': ContentUploadSerializer})
