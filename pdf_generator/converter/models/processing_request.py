from django.db import models

from .recipient import Recipient
from .link_internet_resource import LinkInternetResource


class ProcessingRequest(models.Model):

    recipient_email = models.ForeignKey(
        Recipient,
        on_delete=models.CASCADE,
        related_name='emails',
        verbose_name='Получатель'
    )

    create_datetime = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        verbose_name='Дата создания заявки')

    done_datetime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Дата завершения заявки')

    conversion_file_link = models.URLField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Ссылка на файл для конвертирования'
    )

    conversion_link = models.ForeignKey(
        LinkInternetResource,
        on_delete=models.CASCADE,
        related_name='emails',
        verbose_name='Ссылка на ресурс для конвертирования'
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

    final_file_link = models.URLField(
        max_length=256,
        blank=True,
        unique=True,
        verbose_name='Ссылка на итоговый файл'
    )

    resulting_file_size = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Размер итогового файла'
    )

    class Meta:
        """Meta data."""

        verbose_name = 'Заявка на преобразование в pdf'
        verbose_name_plural = 'Заявки на преобразование в pdf'
