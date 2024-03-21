from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, CommentLike, PostLike, Notification, Category
from .views import toggle_like, BlogList
from .forms import CommentForm, PostForm
from django.utils.text import slugify
from django.contrib.auth.models import User


# Test for toggle_like View
class ToggleLikeTest(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username="testuser", password="12345")
        # Create a post and associate it with the user
        self.post = Post.objects.create(
            title="Test Post", content="Test Content", author=self.user
        )
        # Create a comment and associate it with the post and user
        self.comment = Comment.objects.create(
            post=self.post, content="Test Comment", author=self.user
        )

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
        cls.user = User.objects.create_user(username="testuser", password="12345")

        # Create categories
        cls.category1 = Category.objects.create(name="Category 1")
        cls.category2 = Category.objects.create(name="Category 2")

        # Create posts and assign them to the user
        for i in range(10):
            title = f"Post {i}"
            Post.objects.create(
                title=title,
                slug=slugify(title + "-" + str(i)),  # Use title in slugify
                content="Content",
                author=cls.user,
                category=cls.category1 if i % 2 == 0 else cls.category2,
                status=1,
            )

    def test_blog_list_view_basic(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Post")

    def test_blog_list_view_filtering(self):
        response = self.client.get(reverse("home") + f"?category={self.category1.name}")
        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(len(response.context["post_list"]), 5)

    def test_blog_list_view_sorting_likes(self):
        # You need to add likes to the posts before testing sorting
        response = self.client.get(reverse("home") + "?sort=likes")
        self.assertEqual(response.status_code, 200)

    def test_blog_list_view_sorting_comments(self):
        # You need to add comments to the posts before testing sorting
        response = self.client.get(reverse("home") + "?sort=comments")
        self.assertEqual(response.status_code, 200)

    def test_blog_list_view_pagination_ajax(self):
        # Simulate AJAX request
        factory = RequestFactory()
        request = factory.get(reverse("home"), HTTP_X_REQUESTED_WITH="XMLHttpRequest")

        # Manually attach the user to the request
        request.user = self.user

        response = BlogList.as_view()(request)
        self.assertEqual(response.status_code, 200)


class PostDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="12345")
        cls.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            author=cls.user,
            status=1,
            slug="test-post",  # Explicitly set the slug
        )

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_post_detail_view(self):
        # Access the post detail page
        response = self.client.get(reverse("post_detail", args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.content)

    def test_comment_creation_valid(self):
        # Simulate a logged-in user
        self.client.login(username="testuser", password="12345")

        # Post a valid comment
        response = self.client.post(
            reverse("post_detail", args=[self.post.slug]),
            {"content": "A valid comment"},
        )

        # Check the comment was created and the page redirects back to the post detail
        self.assertEqual(Comment.objects.count(), 1)
        self.assertRedirects(response, reverse("post_detail", args=[self.post.slug]))

    def test_comment_creation_invalid(self):
        # Simulate a logged-in user
        self.client.login(username="testuser", password="12345")

        # Post an invalid comment (empty content)
        response = self.client.post(
            reverse("post_detail", args=[self.post.slug]), {"content": ""}
        )

        # Check the comment was not created
        self.assertEqual(Comment.objects.count(), 0)
        # Check the form is returned with errors
        self.assertTrue(response.context["comment_form"].errors)

    def test_comment_creation_unauthenticated(self):
        # Attempt to post a comment without logging in
        response = self.client.post(
            reverse("post_detail", args=[self.post.slug]), {"content": "A comment"}
        )

        # Check the comment was not created
        self.assertEqual(Comment.objects.count(), 0)
        # Check the response is a redirect to login page or shows an error
        self.assertEqual(response.status_code, 302)


class LikePostViewTest(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

        # Create a user
        self.user = User.objects.create_user(username="testuser", password="12345")

        # Create another user
        self.other_user = User.objects.create_user(
            username="otheruser", password="12345"
        )

        # Create a post
        title = f"Post"
        self.post = Post.objects.create(
            title=title,
            slug=slugify(title + "- 1"),
            content="Test Content",
            author=self.user,
            status=1,
        )

    def test_like_post_authenticated(self):
        # Log in the user
        self.client.login(username="testuser", password="12345")

        # Like the post
        response = self.client.get(reverse("like_post", args=[self.post.slug]))

        # Check the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(PostLike.objects.count(), 1)
        self.assertTrue(
            PostLike.objects.filter(user=self.user, post=self.post).exists()
        )

        # Check the notification
        self.assertEqual(Notification.objects.count(), 1)
        notification = Notification.objects.first()
        self.assertEqual(notification.user, self.post.author)
        self.assertIn(self.post.title, notification.message)

        # Unlike the post
        response = self.client.get(reverse("like_post", args=[self.post.slug]))

        # Check the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(PostLike.objects.count(), 0)

    def test_like_post_unauthenticated(self):
        # Attempt to like the post without logging in
        response = self.client.get(reverse("like_post", args=[self.post.slug]))

        # Check the response
        self.assertEqual(response.status_code, 302)  # Should redirect to login
        self.assertEqual(PostLike.objects.count(), 0)


class DeletePostViewTest(TestCase):

    def setUp(self):
        # Create a post
        title = f"Post"
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.post = Post.objects.create(
            title=title,
            slug=slugify(title + "- 1"),
            content="Test Content",
            author=self.user,
            status=1,
        )
        self.client = Client()
        self.other_user = User.objects.create_user(
            username="otheruser", password="12345"
        )
        self.superuser = User.objects.create_superuser(
            username="superuser", password="12345"
        )

    def test_delete_own_post(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.post(reverse("delete_post", args=[self.post.slug]))
        self.assertRedirects(response, reverse("home"))
        self.assertEqual(Post.objects.count(), 0)

    def test_superuser_delete_post(self):
        self.client.login(username="superuser", password="12345")
        response = self.client.post(reverse("delete_post", args=[self.post.slug]))
        self.assertRedirects(response, reverse("home"))
        self.assertEqual(Post.objects.count(), 0)

    def test_delete_other_user_post(self):
        self.client.login(username="otheruser", password="12345")
        response = self.client.post(reverse("delete_post", args=[self.post.slug]))
        self.assertEqual(response.status_code, 403)  # Forbidden
        self.assertEqual(Post.objects.count(), 1)  # Post should still exist

    def test_unauthenticated_user_delete_post(self):
        response = self.client.post(reverse("delete_post", args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)  # Should redirect to login
        self.assertEqual(Post.objects.count(), 1)  # Post should still exist


class CreatePostViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Test Category", description="Just a test category")
        self.url = reverse("create_post")
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client = Client()

    def test_create_post_authenticated(self):
        self.client.login(username='testuser', password='12345')
        post_data = {
            'title': 'Test Post',
            'content': 'Test Content',
            'category': self.category.name,  # Use category id here
            'status': 1
        }
        response = self.client.post(reverse('create_post'), post_data)

    def test_create_post_form_displayed(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], PostForm)

    def test_create_post_form_invalid(self):
        self.client.login(username="testuser", password="12345")
        post_data = {"title": "", "content": "Test Content", "status": 1}
        response = self.client.post(self.url, post_data)
        self.assertEqual(
            response.status_code, 200
        )  # Stays on the same page due to form errors
        self.assertFalse(Post.objects.filter(content="Test Content").exists())
