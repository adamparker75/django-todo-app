from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        # create an item
        item = Item.objects.create(name='Test Todo Item')
        # Confirm the done status is False
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        # Confirm the name is returned
        self.assertEqual(str(item), 'Test Todo Item')
