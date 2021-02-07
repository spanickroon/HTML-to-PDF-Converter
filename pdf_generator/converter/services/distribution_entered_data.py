"""A module that expands data by methods."""

from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile

from .checking_validity_incoming_data import CheckingValidityIncomingData
from .converter import Converter


class DistributionEnteredData:
    """Class of distribution of received data after post request."""

    @staticmethod
    def procesing_request_by_data_priority(
            file_upload: InMemoryUploadedFile,
            url_upload: str,
            email_upload: str) -> HttpResponse:
        """
        A method that checks the data and then sends it for processing,

        while the file is processed first and then the link.
        Returns the answer without waiting for the execution result,
        because the celety is engaged in other functions.
        """

        checker_data = CheckingValidityIncomingData(file_upload, url_upload)

        if email_upload:
            if file_upload and checker_data.checking_file_validation():
                Converter.converting_html_file_to_pdf(
                    file_upload,
                    email_upload
                )

            if url_upload and checker_data.checking_requested_resource():
                Converter.converting_url_to_pdf(
                    url_upload,
                    email_upload
                )

        return HttpResponse({'status': 'ok'})
