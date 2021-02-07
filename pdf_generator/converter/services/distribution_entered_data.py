from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_framework.response import Response

from .converter_service import ConverterService
from ..serializers import ContentUploadSerializer


class DistributionEnteredData:

    @staticmethod
    def procesing_request_by_data_priority(
            file_upload: InMemoryUploadedFile,
            url_upload: str,
            email_upload: str) -> Response:

        checker_data = CheckingValidityIncomingData(file_upload, url_upload)

        if email_upload:
            if file_upload and checker_data.checking_file_validation():
                ConverterService.converting_html_file_to_pdf(file_upload)

            if url_upload and checker_data.checking_requested_resource():
                ConverterService.converting_url_to_pdf(url_upload)

        return Response({'serializer': ContentUploadSerializer})
