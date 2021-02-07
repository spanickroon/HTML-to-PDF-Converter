"""Class test module DistributionEnteredData."""

from django.test import TestCase
from unittest.mock import patch

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse

from ..services.distribution_entered_data import DistributionEnteredData
from ..services.checking_validity_incoming_data import \
    CheckingValidityIncomingData


class DistributionEnteredDataTest(TestCase):
    """DistributionEnteredDataTest."""

    def setUp(self):
        self.test_file = InMemoryUploadedFile(
            file='test', field_name='test', name='test',
            content_type='text/html', size=64, charset='UTF-8'
        )
        self.test_link = 'https://test.com'
        self.test_email = 'test@test.test'
        self.test_func = \
            DistributionEnteredData.procesing_request_by_data_priority

    @patch.object(CheckingValidityIncomingData, 'checking_file_validation')
    @patch.object(CheckingValidityIncomingData, 'checking_requested_resource')
    def test_procesing_request_by_data_priority(self, file_mock, request_mock):
        file_mock.return_value = False
        request_mock.return_value = False

        result = self.test_func(
            file_upload=self.test_file,
            url_upload=self.test_link,
            email_upload=self.test_email
        )

        test_result = HttpResponse({'status': 'ok'})

        self.assertEqual(result.status_code, test_result.status_code)
        self.assertEqual(result.content, test_result.content)
