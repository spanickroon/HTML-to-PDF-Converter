"""Module containing celery tasks."""

from .converter_service import ConverterService
from .sending_email import MessageSender
from celery.decorators import task


@task
def celery_task_converting_html(task_id: int, final_file_name: str) -> None:
    """A function that launches a celery task for converting a file to pdf."""
    ConverterService.converting_from_file(task_id, final_file_name)
    MessageSender.sending_pdf_file(task_id)


@task
def celery_task_converting_url(task_id: int, final_file_name: str) -> None:
    """A function that launches a celery task for converting a url to pdf."""
    ConverterService.converting_from_url(task_id, final_file_name)
    MessageSender.sending_pdf_file(task_id)
