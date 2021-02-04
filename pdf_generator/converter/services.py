import os
import pdfkit

from django.conf import settings
from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile


class ConverterService:

    @staticmethod
    def creating_path_for_converting_files() -> str:
        MCFR = settings.MEDIA_CONVERTING_FILES_ROOT

        if not os.path.exists(MCFR):
            os.makedirs(MCFR)

        return MCFR

    @staticmethod
    def converting_html_file_to_pdf(
            html_file: InMemoryUploadedFile) -> HttpResponse:

        MCFR = ConverterService.creating_path_for_converting_files()

        with open(os.path.join(MCFR, 'output.html'), 'w+b') as wf:
            wf.write(html_file.read())

        pdfkit.from_file(
            os.path.join(MCFR, 'output.html'),
            os.path.join(MCFR, 'output.pdf')
        )

        with open(os.path.join(MCFR, 'output.pdf'), 'rb') as rf:
            return HttpResponse(rf.read(), 'application/pdf')

    @staticmethod
    def converting_url_to_pdf(url: str) -> HttpResponse:
        MCFR = ConverterService.creating_path_for_converting_files()

        output_html = os.path.join(MCFR, 'output.html')
        pdfkit.from_url(url, output_html)

        with open(output_html, 'rb') as rf:
            return HttpResponse(rf.read(), 'application/pdf')
