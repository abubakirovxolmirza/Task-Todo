from django.test import TestCase
from apps.todo.models import Todo
from apps.users.models import User

class TodoModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword123'
        )
        self.todo = Todo.objects.create(
            user=self.user,
            title='Test Todo',
            description='Test description for the todo item.'
        )
    
    def test_todo_creation(self):
        self.assertEqual(self.todo.title, 'Test Todo')
        self.assertEqual(self.todo.description, 'Test description for the todo item.')
        self.assertEqual(self.todo.user, self.user)
    
    def test_todo_str(self):
        self.assertEqual(str(self.todo), 'Test Todo')
    
    def test_auto_timestamps(self):
        self.assertIsNotNone(self.todo.created_at)
        self.assertIsNotNone(self.todo.updated_at)
