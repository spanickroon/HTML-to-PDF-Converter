import os
import pdfkit
import tempfile
import requests

from django.core.files.storage import default_storage

from datetime import datetime

from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_framework.response import Response

from ..models import ProcessingRequest
from django.contrib.auth.models import User

from django.core.files.base import ContentFile


class ConverterService:

    @staticmethod
    def _generate_file_name(email_upload: str, file_type: str) -> str:
        file_name = []
        time_now = datetime.now().strftime('%m.%d.%Y %H.%M.%S')

        file_name.append(email_upload)
        file_name.append(time_now)
        file_name.append(str(hash(time_now + email_upload)))
        file_name.append(file_type)

        return '_'.join(file_name)

    @staticmethod
    def _create_new_file_request(
            html_file: InMemoryUploadedFile,
            email_upload: str) -> int:
        recipient, _ = User.objects.get_or_create(
            username=email_upload, email=email_upload)

        html_file.name = ConverterService._generate_file_name(
            email_upload, '.html')

        task_hash = hash(html_file.name)

        new_request = ProcessingRequest(
            user=recipient,
            conversion_file=html_file,
            task_id=task_hash,
            status=1
        )

        new_request.save()

        return task_hash

    @staticmethod
    def converting_from_file(task_id: int, final_file_name: str) -> None:
        recipient = ProcessingRequest.objects.get(task_id=task_id)
        recipient.status = 2

        with tempfile.NamedTemporaryFile(suffix='.html') as temp_html:
            with tempfile.NamedTemporaryFile(suffix='.pdf') as temp_pdf:
                content = requests.get(recipient.conversion_file.url).content
                temp_html.write(content)
                pdfkit.from_file(
                    temp_html.name,
                    temp_pdf.name
                )
                recipient.final_file = ContentFile(
                    temp_pdf.read(),
                    f'{final_file_name}'
                )

        recipient.save()

    @staticmethod
    def converting_html_file_to_pdf(
            html_file: InMemoryUploadedFile,
            email_upload: str) -> HttpResponse:

        try:
            task_id = ConverterService._create_new_file_request(
                html_file,
                email_upload
            )

            final_file_name = ConverterService._generate_file_name(
                email_upload, '.pdf')

        except (OSError, AttributeError):
            return HttpResponse('error')

        ConverterService.converting_from_file(task_id, final_file_name)

        return HttpResponse('ok')

    """
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
    """
