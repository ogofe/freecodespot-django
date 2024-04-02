# from django.test import TestCase
# from django.urls import reverse
# from .models import TodoListItem
# from django.db.models import QuerySet
# # import unittest.runner


# class TodoAppTestCase(TestCase):
#     def setUp(self):
#         TodoListItem.objects.create(label="Drink some water", done=False)
#         TodoListItem.objects.create(label="Create a Todo Test", done=True)

#     def test_get_todos(self):
#         response = self.client.get(reverse('todo:home'))
#         todo_list:QuerySet = response.context['todo_list']
#         # print("Response:", todo_list)
#         # self.assertEqual(response.status_code, 200)
#         self.assertIn("Drink some water", todo_list.all())
#         # self.assertIn("Create a Todo Test", todo_list)
        

#     def test_create_todo(self):
#         response = self.client.post(reverse('todo:home'), {'label': 'New Todo', 'done': False})
#         # self.assertEqual(response.status_code, 201)
#         self.assertTrue(TodoListItem.objects.filter(label='New Todo').exists())

# # todo_test = unittest.loader.makeSuite(TodoAppTestCase)
# # todo_test
