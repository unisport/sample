from django.test import TestCase

from management.commands import get_fixtures


class GetFixturesTest(TestCase):
    def test_json_format(self):
        fixtures = get_fixtures.download_json()
        self.assertIsInstance(fixtures, dict)
