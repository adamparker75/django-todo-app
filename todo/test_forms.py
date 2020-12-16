from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        # Create the form sending no name
        form = ItemForm({'name', ''})
        # Ensures the form is not valid
        self.assertFalse(form.is_valid())
        # Asserts whether there is a name key in the errors
        self.assertIn('name', form.errors.keys)
        # Checks if the error on the name field is the required one
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        # Create the form sending a name
        form = ItemForm({'name': 'Test Todo Item'})
        # Tests the form is valid
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
