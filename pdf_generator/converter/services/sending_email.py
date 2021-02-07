"""A module containing a class for sending letters to mail """

from django.core.mail import EmailMessage
from ..models import ProcessingRequest


class MessageSender:
    """A class that sends a message to mail."""

    @staticmethod
    def sending_pdf_file(task_id: int) -> None:
        """
        A method that edits the finished pdf file as a link to mail.

        Accepts ID tasks and executes them last in the chain.
        By id, it gets the desired object and pulls out the data that
        was put in the methods earlier. Sets the status of the task to ready.
        """
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
