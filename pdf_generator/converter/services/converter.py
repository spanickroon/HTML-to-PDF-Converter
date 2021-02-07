from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile

from .converter_service import ConverterService
from .tasks import celery_task_converting_html, celery_task_converting_url


class Converter:

    @staticmethod
    def converting_html_file_to_pdf(
            html_file: InMemoryUploadedFile,
            email_upload: str) -> None:

        try:
            task_id = ConverterService._create_new_request(
                email_upload=email_upload,
                conversion_url=None,
                conversion_file=html_file
            )

            final_file_name = ConverterService._generate_file_name(
                email_upload, '.pdf')

        except (OSError, AttributeError, FileNotFoundError):
            pass

        celery_task_converting_html(task_id, final_file_name)

    @staticmethod
    def converting_url_to_pdf(
            url_upload: str,
            email_upload: str) -> None:
        try:
            task_id = ConverterService._create_new_request(
                email_upload=email_upload,
                conversion_url=url_upload,
                conversion_file=None
            )

            final_file_name = ConverterService._generate_file_name(
                email_upload, '.pdf')

        except (OSError, AttributeError, FileNotFoundError):
            pass

        celery_task_converting_url(task_id, final_file_name)
