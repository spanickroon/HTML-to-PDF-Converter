"""Application serializers module."""

from rest_framework.serializers import (
    Serializer,
    FileField,
    URLField,
    EmailField
)


class ContentUploadSerializer(Serializer):
    """
    A serializer class.

    Containing three fields: for file, for link, and for email.
    """

    file_upload = FileField()
    url_upload = URLField()
    email_upload = EmailField()

    class Meta:
        """Meta data."""

        fields = ['file_uploaded', 'url_upload', 'email_upload']
