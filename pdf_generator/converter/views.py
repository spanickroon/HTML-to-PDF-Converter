from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.renderers import TemplateHTMLRenderer

from django.http import HttpResponse
from .serializers import ContentUploadSerializer
from .services import DistributionEnteredData


class ContentUploadViewSet(ViewSet):

    serializer_class = ContentUploadSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'converting_data.html'

    def create(self, request: Request) -> Response:
        file_upload = request.data.get('file_upload')
        url_upload = request.data.get('url_upload')
        email_upload = request.data.get('email_upload')

        return DistributionEnteredData.procesing_request_by_data_priority(
            file_upload,
            url_upload,
            email_upload
        )

    def retrieve(self, request: Request) -> Response:
        return Response({'serializer': ContentUploadSerializer})
