"""Module with a model of requests for processing."""

from django.db import models
from django.contrib.auth.models import User

from .link_internet_resource import LinkInternetResource


class ProcessingRequest(models.Model):
    """
    Model with a request for processing or file or link.

    Consists of fields:
        *user - binding from the standard model via email;
        *create_datetime - time of order creation;
        *conversion_file - file for processing, can be empty if a link to an
            Internet resource is sent;
        *conversion_url - processing link, can be empty if file is transferred;
        *task_id - id of the task that performs transformations
            with the transmitted data;
        *status - the status of the request can be of three types:
            in processing, in progress and ready;
        *final_file - conversion result, link to pdf file.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Получатель'
    )

    create_datetime = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        verbose_name='Дата создания заявки')

    conversion_file = models.FileField(
        upload_to='documents/html',
        blank=True,
        null=True,
        verbose_name='Html файл для конвертирования'
    )

    conversion_url = models.ForeignKey(
        LinkInternetResource,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Ссылка на ресурс для конвертирования'
    )

    task_id = models.BigIntegerField(
        blank=True,
        null=True,
        verbose_name='ID задачи'
    )

    STATUS_CHOICES = (
        (1, 'В ожидании'),
        (2, 'В процессе'),
        (3, 'Готово')
    )

    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES,
        blank=True,
        null=True,
        verbose_name='Статус заявки',
    )

    final_file = models.FileField(
        upload_to='documents/pdf',
        blank=True,
        null=True,
        verbose_name='Итоговый файл pdf'
    )

    class Meta:
        """Meta data."""

        verbose_name = 'Заявка на преобразование в pdf'
        verbose_name_plural = 'Заявки на преобразование в pdf'

    def __str__(self) -> str:
        """Magic method that returns a reference when working with a model."""
        return f'{self.user.email} - {self.status}'
