"""The module in which the selection of tasks occurs."""

from django.core.files.uploadedfile import InMemoryUploadedFile

from .converter_service import ConverterService
from .tasks import celery_task_converting_html, celery_task_converting_url


class Converter:
    """The class that is responsible for the conversion."""

    @staticmethod
    def converting_html_file_to_pdf(
            html_file: InMemoryUploadedFile,
            email_upload: str) -> None:
        """
        A method that creates a request for data preparation file conversion

        and calls a celery task that runs in the background.
        """
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
        except Exception as ex:
            pass

        celery_task_converting_html.delay(task_id, final_file_name)

    @staticmethod
    def converting_url_to_pdf(
            url_upload: str,
            email_upload: str) -> None:
        """
        A method that creates a request for data preparation url conversion

        and calls a celery task that runs in the background.
        """
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
        except Exception as ex:
            pass

        celery_task_converting_url.delay(task_id, final_file_name)
