from django.db import models


class Recipient(models.Model):

    email = models.EmailField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Получатель'
    )

    class Meta:
        """Meta data."""

        verbose_name = 'Пользователь ресурса'
        verbose_name_plural = 'Список пользователей ресурса'
