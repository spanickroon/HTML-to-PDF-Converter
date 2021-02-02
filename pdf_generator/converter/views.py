from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import ContentUploadSerializer
from .services import ConverterService
from django.http import HttpResponse


class ContentUploadViewSet(ViewSet):
    serializer_class = ContentUploadSerializer

    def create(self, request: Request) -> Response:
        response = Response()

        file_upload = request.data.get('file_upload')
        url_upload = request.data.get('url_upload')

        if file_upload:
            ConverterService.converting_html_file_to_pdf(file_upload)

        # if url_upload:
            # response.append(url_upload)

        return ConverterService.returning_file_information(file_upload)

    def retrieve(self, request: Request):
        return HttpResponse('test')
