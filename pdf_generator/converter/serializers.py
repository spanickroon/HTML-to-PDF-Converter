from rest_framework.serializers import Serializer, FileField, URLField


class ContentUploadSerializer(Serializer):

    file_upload = FileField()
    url_upload = URLField()

    class Meta:
        fields = ['file_uploaded', 'url_upload']
