from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='test group',
            slug='test slug',
            description='Test description',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='test post',
        )

    def setUp(self):
        self.post = PostModelTest.post
        self.group = PostModelTest.group

    def test_models_have_correct_object_names(self):
        """__str__ works correctly for models."""
        post_expected_name = self.post.text[:15]
        self.assertEqual(
            post_expected_name,
            str(self.post),
            'Post title error'
        )

        group_expected_name = self.group.title
        self.assertEqual(
            group_expected_name,
            str(self.group),
            'Group name output error'
        )

    def test_verbose_name(self):
        """verbose_name in the fields is the same as expected."""
        field_verboses = {
            'text': 'Post text',
            'pub_date': 'Publication date',
            'author': 'Author',
            'group': 'Group',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.post._meta.get_field(value).verbose_name, expected)

    def test_help_text(self):
        """help_text in the fields is the same as expected."""
        field_help_texts = {
            'text': 'Enter your post text',
            'group': 'The group to which the post belongs'
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.post._meta.get_field(value).help_text, expected)
