"""Module with models for links."""

from django.db import models


class LinkInternetResource(models.Model):
    """
    The class that stores unique Internet resource.

    Has one field - a link to the resource.
    """

    link = models.URLField(
        max_length=256,
        blank=True,
        unique=True,
        verbose_name='Ссылка на ресурс для преобразования'
    )

    class Meta:
        """Meta data."""

        verbose_name = 'Ссылка на интернет ресурс'
        verbose_name_plural = 'Ссылки на интернет ресурс'

    def __str__(self) -> str:
        """Magic method that returns a reference when working with a model."""
        return self.link
