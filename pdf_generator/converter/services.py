import requests
from bs4 import BeautifulSoup
from io import BytesIO
from xhtml2pdf import pisa

from rest_framework.response import Response
from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile


class ConverterService:

    @staticmethod
    def converting_html_file_to_pdf(html_file: bytes) -> HttpResponse:
        pdf_file = BytesIO()
        pisa_obj = pisa.pisaDocument(html_file, pdf_file)

        if not pisa_obj.err:
            return HttpResponse(
                pdf_file.getvalue(),
                content_type='application/pdf'
            )

        return HttpResponse()

    @staticmethod
    def returning_file_information(
            html_file: InMemoryUploadedFile) -> Response:
        return Response({
            'name': html_file.name,
            'type': html_file.content_type,
            'size': html_file.size
        })


class HTMLScraperService:

    @staticmethod
    def scraping_html(url: str) -> BeautifulSoup:
        return BeautifulSoup(requests.get(url).content, 'html.parser')
