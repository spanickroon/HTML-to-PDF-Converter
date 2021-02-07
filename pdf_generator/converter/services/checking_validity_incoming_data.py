import requests

from django.core.files.uploadedfile import InMemoryUploadedFile


class CheckingValidityIncomingData:

    def __init__(
            self, file_upload: InMemoryUploadedFile,
            url_upload: str) -> None:
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
