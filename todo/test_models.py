from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defualts_to_fasle(self):
        item = Item.objects.create(name="Test Todo Item")
        # checking done status is false
        self.assertFalse(item.done)

    def test_item_string_method_name(self):
        item = Item.objects.create(name="Test Todo Item")
        self.assertEqual(str(item), 'Test Todo Item')
