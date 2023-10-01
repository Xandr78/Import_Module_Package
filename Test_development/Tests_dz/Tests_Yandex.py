from Yandex_API import create_folder, status_code
from unittest import TestCase

class YandexTestCase(TestCase):
    def test_create_folder(self):
        res = create_folder('STAR WARS')
        self.assertTrue(res==201, f'ok')

    def test_status_code(self):
        res = status_code('STAR WARS')
        self.assertTrue(res == 'OK')
