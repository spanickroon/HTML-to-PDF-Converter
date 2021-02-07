"""Data validation test module."""

from django.test import TestCase


from ..services.checking_validity_incoming_data import \
    CheckingValidityIncomingData


class CheckingValidityIncomingDataTest(TestCase):
    """Test CheckingValidityIncomingData."""

    def setUp(self):
        self.test_obj = CheckingValidityIncomingData('test', 'http://test')

    def test_checking_file_validation(self):
        self.assertEqual(self.test_obj.checking_file_validation(), False)

    def test_checking_requested_resource(self):
        self.assertEqual(self.test_obj.checking_requested_resource(), False)
