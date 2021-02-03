from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import ContentUploadSerializer
from .services import ConverterService, HTMLScraperService


class ContentUploadViewSet(ViewSet):

    serializer_class = ContentUploadSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'converting_data.html'

    def create(self, request: Request) -> Response:
        file_upload = request.data.get('file_upload')
        url_upload = request.data.get('url_upload')

        if file_upload:
            return ConverterService.converting_html_file_to_pdf(file_upload.read())

        if url_upload:
            html_file = HTMLScraperService.scraping_html(url_upload).encode()
            return ConverterService.converting_html_file_to_pdf(html_file)

        return Response({'serializer': ContentUploadSerializer})

    def retrieve(self, request: Request) -> Response:
        return Response({'serializer': ContentUploadSerializer})
