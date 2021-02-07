from django.db import models
from django.contrib.auth.models import User

from .link_internet_resource import LinkInternetResource


class ProcessingRequest(models.Model):

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

    done_datetime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Дата завершения заявки')

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

    resulting_file_size = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Размер итогового файла'
    )

    class Meta:
        """Meta data."""

        verbose_name = 'Заявка на преобразование в pdf'
        verbose_name_plural = 'Заявки на преобразование в pdf'

    def __str__(self) -> str:
        return f'{self.user.email} - {self.status}'
