from .converter_service import ConverterService
from .sending_email import MessageSender


def celery_task_converting_html(task_id: int, final_file_name: str) -> None:
    ConverterService.converting_from_file(task_id, final_file_name)
    MessageSender.sending_pdf_file(task_id)


def celery_task_converting_url(task_id: int, final_file_name: str) -> None:
    ConverterService.converting_from_url(task_id, final_file_name)
    MessageSender.sending_pdf_file(task_id)
