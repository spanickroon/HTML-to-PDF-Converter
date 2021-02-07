import os
import pdfkit
import requests

from django.conf import settings
from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_framework.response import Response

from .serializers import ContentUploadSerializer


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


class CheckingValidityIncomingData:

    def __init__(self, file_upload: InMemoryUploadedFile, url_upload: str):
        self.file_upload = file_upload
        self.url_upload = url_upload

    def checking_file_validation(self) -> bool:
        try:
            return self.file_upload.content_type == 'text/html'
        except AttributeError:
            return False

    def checking_requested_resource(self) -> bool:
        try:
            requests.get(self.url_upload)
            return True
        except requests.exceptions.ConnectionError:
            return False


class DistributionEnteredData:

    @staticmethod
    def procesing_request_by_data_priority(
            file_upload: InMemoryUploadedFile,
            url_upload: str,
            email_upload: str) -> Response:

        checker_data = CheckingValidityIncomingData(file_upload, url_upload)

        if file_upload and checker_data.checking_file_validation():
            return ConverterService.converting_html_file_to_pdf(file_upload)

        if url_upload and checker_data.checking_requested_resource():
            return ConverterService.converting_url_to_pdf(url_upload)

        return Response({'serializer': ContentUploadSerializer})
