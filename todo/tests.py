from django.test import TestCase
from .models import TodoListItem as Todo
from django.urls import reverse

class TodoAppTestCase(TestCase):
    def setUp(self):
        Todo.objects.create(label="Drink some water", done=False)
        Todo.objects.create(label="Create a Todo Test", done=True)

    def test_get_todos(self):
        response = self.client.get(reverse('todo:home'))
        self.assertEqual(response.status_code, 200)
        todos = [ todo.label for todo in response.context['todo_list']]
        print('response', todos)
        self.assertTrue("Drink some water" in todos)

    def test_create_todo(self):
        response = self.client.post(reverse('todo:home'), {'label': 'New Todo', 'done': False})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(label='New Todo').exists())

    def test_status_code(self):
        response = self.client.get(reverse('todo:home'))
        self.assertTrue(response.status_code == 200)

    def test_false_status_code(self):
        response = self.client.get(reverse('todo:home'))
        # should fail since we're expecting a 200 response
        self.assertEqual(response.status_code, 500)
