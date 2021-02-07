import os
import time

import pdfkit
import tempfile
import requests

from datetime import datetime

from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import User

from rest_framework.response import Response

from ..models import ProcessingRequest, LinkInternetResource


class ConverterService:

    @staticmethod
    def _generate_file_name(email_upload: str, file_type: str) -> str:
        file_name = []
        time_now = datetime.now().strftime('%d.%m.%Y %H.%M.%S')

        file_name.append(email_upload)
        file_name.append(time_now)
        file_name.append(str(hash(time_now + email_upload)))
        file_name.append(file_type)

        return '_'.join(file_name)

    @staticmethod
    def _create_new_request(
            email_upload: str,
            conversion_url: str,
            conversion_file: InMemoryUploadedFile) -> int:

        recipient, _ = User.objects.get_or_create(
            username=email_upload,
            email=email_upload)

        if conversion_file:
            conversion_file.name = ConverterService._generate_file_name(
                email_upload, '.html')

        if conversion_url:
            conversion_url, _ = LinkInternetResource.objects.get_or_create(
                link=conversion_url
            )

        task_hash = hash(time.time())

        new_request = ProcessingRequest(
            user=recipient,
            conversion_url=conversion_url,
            conversion_file=conversion_file,
            task_id=task_hash,
            status=1
        )

        new_request.save()

        return task_hash

    @staticmethod
    def converting_from_file(task_id: int, final_file_name: str) -> None:
        recipient = ProcessingRequest.objects.get(task_id=task_id)
        recipient.status = 2

        with open(f'{final_file_name}.html', 'w+b') as temp_html:
            content = requests.get(recipient.conversion_file.url).content
            temp_html.write(content)

        pdfkit.from_file(f'{final_file_name}.html', f'{final_file_name}')

        with open(f'{final_file_name}', 'rb') as temp_pdf:
            recipient.final_file = ContentFile(
                temp_pdf.read(),
                f'{final_file_name}'
            )

        recipient.save()

        os.remove(f'{final_file_name}.html')
        os.remove(f'{final_file_name}')

    @staticmethod
    def converting_from_url(task_id: int, final_file_name: str) -> None:
        recipient = ProcessingRequest.objects.get(task_id=task_id)
        recipient.status = 2

        with open(f'{final_file_name}', 'w+b') as temp_pdf:
            pass

        pdfkit.from_url(recipient.conversion_url.link,  f'{final_file_name}')

        with open(f'{final_file_name}', 'rb') as temp_pdf:
            recipient.final_file = ContentFile(
                    temp_pdf.read(),
                    f'{final_file_name}'
                )

        recipient.save()
        os.remove(f'{final_file_name}')
