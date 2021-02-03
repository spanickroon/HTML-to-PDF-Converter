from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse
from rest_framework.response import Response


from django.core.files.uploadedfile import InMemoryUploadedFile


class ConverterService:

    @staticmethod
    def converting_html_file_to_pdf(html_file: InMemoryUploadedFile):
        pdf_file = BytesIO()
        pisa_obj = pisa.pisaDocument(html_file.read(), pdf_file)

        if not pisa_obj.err:
            return HttpResponse(
                pdf_file.getvalue(),
                content_type='application/pdf'
            )

        return Response()

    @staticmethod
    def returning_file_information(
            html_file: InMemoryUploadedFile) -> Response:
        return Response({
            'name': html_file.name,
            'type': html_file.content_type,
            'size': html_file.size
        })
