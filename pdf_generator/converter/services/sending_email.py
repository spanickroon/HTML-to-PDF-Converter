from django.core.mail import EmailMessage
from ..models import ProcessingRequest


class MessageSender:

    @staticmethod
    def sending_pdf_file(task_id: int) -> None:
        new_request = ProcessingRequest.objects.get(task_id=task_id)

        user = new_request.user.email
        link = new_request.final_file.url

        mail = EmailMessage(
            subject='PDF converter',
            body=f'Hello, {user}\n\nYour file:\n{link}',
            to=[user]
        )

        mail.send()

        new_request.status = 3

        new_request.save()
