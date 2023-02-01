from django.test import TestCase
from .models import Item


class TestViews(TestCase):
    # self refers to TestDjango class
    def test_get_todo_list(self):
        response = self.client.get('/')
        # 200, sucessfull http response
        self.assertEqual(response.status_code, 200)
        # check correct template
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        # 200, sucessfull http response
        self.assertEqual(response.status_code, 200)
        # check correct template
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        # 200, sucessfull http response
        self.assertEqual(response.status_code, 200)
        # check correct template
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        # prove item is deleted
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        # check done status
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(
            f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
