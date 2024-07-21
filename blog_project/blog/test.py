from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create(title='Test Post', content='Content of the test post', author=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'Content of the test post')
        self.assertEqual(self.post.author.username, 'testuser')

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create(title='Test Post', content='Content of the test post', author=self.user)
        self.comment = Comment.objects.create(post=self.post, author='commenter', text='Test comment')

    def test_comment_creation(self):
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.author, 'commenter')
        self.assertEqual(self.comment.text, 'Test comment')
