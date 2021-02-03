from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import ContentUploadSerializer
from .services import ConverterService
from django.http import HttpResponse

from rest_framework.renderers import TemplateHTMLRenderer


class ContentUploadViewSet(ViewSet):

    serializer_class = ContentUploadSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'converting_data.html'

    def create(self, request: Request) -> Response:
        response = Response()

        file_upload = request.data.get('file_upload')
        url_upload = request.data.get('url_upload')

        if file_upload:
            return ConverterService.converting_html_file_to_pdf(file_upload)

        # if url_upload:
            # response.append(url_upload)

        return Response({'serializer': ContentUploadSerializer})

    def retrieve(self, request: Request) -> Response:
        return Response({'serializer': ContentUploadSerializer})
