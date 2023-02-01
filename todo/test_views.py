from django.test import TestCase


class TestDjango(TestCase):
    # self refers to TestDjango class
    def test_this_thing_works(self):
        self.assertEqual(1, 1)
