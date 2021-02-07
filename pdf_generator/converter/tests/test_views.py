"""View testing module."""

from django.test import TestCase


class ContentUploadViewSetTest(TestCase):
    """ContentUploadViewSetTest."""

    def test_view_get_request(self):
        response = self.client.get('/converter/')
        self.assertEqual(response.status_code, 200)

    def test_view_post_request(self):
        response = self.client.post('/converter/')
        self.assertEqual(response.status_code, 200)
