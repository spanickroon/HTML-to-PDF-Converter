import os
import pdfkit
import requests

from django.conf import settings
from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_framework.response import Response


class ConverterService:

    output_html = 'output.html'
    output_pdf = 'output.pdf'

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

        try:
            file_path = os.path.join(MCFR, ConverterService.output_html)

            with open(file_path, 'w+b') as wf:
                wf.write(html_file.read())

            pdfkit.from_file(
                os.path.join(MCFR, ConverterService.output_html),
                os.path.join(MCFR, ConverterService.output_pdf)
            )

            file_path = os.path.join(MCFR, ConverterService.output_pdf)

            with open(os.path.join(MCFR, file_path), 'rb') as rf:
                return HttpResponse(rf.read(), 'application/pdf')
        except OSError:
            return HttpResponse('error')

    @staticmethod
    def converting_url_to_pdf(url: str) -> HttpResponse:
        MCFR = ConverterService.creating_path_for_converting_files()

        try:
            file_path = os.path.join(MCFR, ConverterService.output_pdf)

            pdfkit.from_url(url, file_path)

            with open(file_path, 'rb') as rf:
                return HttpResponse(rf.read(), 'application/pdf')
        except OSError:
            return HttpResponse('error')
