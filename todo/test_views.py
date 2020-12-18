from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_get_todo_list(self):
        # To test the HTTP response of the view
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # To confirm the view uses the correct template
        # And tell it the templatre we expect
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # Create a DB item to use
        item = Item.objects.create(name='Test Todo Item')
        # We pass in the URL followed by an item ID
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # Tests adding an item to the DB
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # Redirect back to the home page
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        # Create a DB item
        item = Item.objects.create(name='Test Todo Item')
        # Deletes the item from the DB
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        # To prove the item is deleted try to get from the
        # Db using it's ID
        existing_items = Item.objects.filter(id=item.id)
        # Check the lenght of existing items in the DB
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # Create a DB item
        item = Item.objects.create(name='Test Todo Item', done=True)
        # Deletes the item from the DB
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        # Post an updated name
        response = self.client.post(
            f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
