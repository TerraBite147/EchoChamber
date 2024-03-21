from django.test import TestCase
from .forms import CommentForm, PostForm
from .models import Category 

# Create your tests here.

class CommentFormTest(TestCase):

    def test_comment_form_valid_data(self):
        form = CommentForm(data={'content': 'A test comment'})
        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1) 


class PostFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a category for the test post
        cls.category = Category.objects.create(name='Test Category')

    def test_post_form_valid_data(self):
        form = PostForm(data={
            'title': 'Test Post',
            'category': self.category.id,
            'content': 'Some content for the test post',
            'excerpt': 'Test excerpt',
            'status': 1
        })
        self.assertTrue(form.is_valid())
    
    def test_post_form_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        # Check for the number of errors
        self.assertEqual(len(form.errors), 5)