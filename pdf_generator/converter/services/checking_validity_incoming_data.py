"""
Module containing checks.

for the availability of the Internet resource and file type.
"""

import requests
import logging

from django.core.files.uploadedfile import InMemoryUploadedFile


class CheckingValidityIncomingData:
    """A class containing methods for checking the file and links."""

    def __init__(
            self, file_upload: InMemoryUploadedFile,
            url_upload: str) -> None:
        """The class constructor takes a file and a link."""
        self.file_upload = file_upload
        self.url_upload = url_upload

    def checking_file_validation(self) -> bool:
        """File Type Matching Check."""
        try:
            return self.file_upload.content_type == 'text/html'
        except AttributeError as ex:
            logging.error(ex)
            return False

    def checking_requested_resource(self) -> bool:
        """Checking the possibility of getting a response from the link."""
        try:
            requests.get(self.url_upload)
            return True
        except requests.exceptions.ConnectionError as ex:
            logging.error(ex)
            return False
