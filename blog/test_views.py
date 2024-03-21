from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, PostLike, CommentLike, Category
from .views import toggle_like, BlogList
from django.utils.text import slugify


# Test for toggle_like View
class ToggleLikeTest(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Create a post and associate it with the user
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        # Create a comment and associate it with the post and user
        self.comment = Comment.objects.create(post=self.post, content='Test Comment', author=self.user)

    def test_toggle_like_post(self):
        # Test liking the post
        self.assertTrue(toggle_like(self.post, self.user))
        self.assertEqual(PostLike.objects.count(), 1)
        
        # Test unliking the post
        self.assertFalse(toggle_like(self.post, self.user))
        self.assertEqual(PostLike.objects.count(), 0)

    def test_toggle_like_comment(self):
        # Test liking the comment
        self.assertTrue(toggle_like(self.comment, self.user))
        self.assertEqual(CommentLike.objects.count(), 1)
        self.assertEqual(self.comment.likes.count(), 1)
        
        # Test unliking the comment
        self.assertFalse(toggle_like(self.comment, self.user))
        self.assertEqual(CommentLike.objects.count(), 0)
        self.assertEqual(self.comment.likes.count(), 0)


# Test for BlogList View
class BlogListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.user = User.objects.create_user(username='testuser', password='12345')

        # Create categories
        cls.category1 = Category.objects.create(name='Category 1')
        cls.category2 = Category.objects.create(name='Category 2')

        # Create posts and assign them to the user
        for i in range(10):
            title = f'Post {i}'
            Post.objects.create(
                title=title,
                slug=slugify(title + "-" + str(i)),  # Use title in slugify
                content='Content',
                author=cls.user,
                category=cls.category1 if i % 2 == 0 else cls.category2,
                status=1
            )

    def test_blog_list_view_basic(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post')

    def test_blog_list_view_filtering(self):
        response = self.client.get(reverse('home') + f'?category={self.category1.name}')
        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(len(response.context['post_list']), 5)

    def test_blog_list_view_sorting_likes(self):
        # You need to add likes to the posts before testing sorting
        response = self.client.get(reverse('home') + '?sort=likes')
        self.assertEqual(response.status_code, 200)

    def test_blog_list_view_sorting_comments(self):
        # You need to add comments to the posts before testing sorting
        response = self.client.get(reverse('home') + '?sort=comments')
        self.assertEqual(response.status_code, 200)

    def test_blog_list_view_pagination_ajax(self):
        # Simulate AJAX request
        factory = RequestFactory()
        request = factory.get(reverse('home'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        
        # Manually attach the user to the request
        request.user = self.user
        
        response = BlogList.as_view()(request)
        self.assertEqual(response.status_code, 200)
