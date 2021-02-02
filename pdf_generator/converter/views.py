from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import ContentUploadSerializer


class ContentUploadViewSet(ViewSet):
    serializer_class = ContentUploadSerializer

    def create(self, request: Request) -> Response:
        response = []

        if request.data.get('file_upload'):
            response.append(request.FILES.get('file_upload'))

        if request.data.get('url_upload'):
            response.append(request.data.get('url_upload'))

        return Response(response)
