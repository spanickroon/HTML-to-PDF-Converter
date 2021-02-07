from rest_framework.serializers import (
    Serializer,
    FileField,
    URLField,
    EmailField
)


class ContentUploadSerializer(Serializer):

    file_upload = FileField()
    url_upload = URLField()
    email_upload = EmailField()

    class Meta:
        fields = ['file_uploaded', 'url_upload', 'email_upload']
