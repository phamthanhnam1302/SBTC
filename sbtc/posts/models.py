from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from taggit.managers import TaggableManager


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=20, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Community'
        verbose_name_plural = 'Communities'
        ordering = ('title',)


class Post(models.Model):
    text = models.TextField(
        'Post text',
        help_text='Enter your post text'
    )
    pub_date = models.DateTimeField(
        'Publication date',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Author'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Group',
        help_text='Group to which the post belongs'
    )
    image = models.ImageField(
        'Picture',
        upload_to='posts/',
        blank=True
    )
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.text[:settings.POST_STRING_TITLE]

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Fast'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='A comment',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Comment author'
    )
    text = models.TextField(
        'Comment text',
        help_text='New comment text'
    )
    created = models.DateTimeField(
        'Comment date',
        auto_now_add=True
    )

    def __str__(self):
        return self.text[:settings.POST_STRING_TITLE]

    class Meta:
        verbose_name = 'A comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created',)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='User',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Author'
    )

    def __str__(self):
        return f'{self.user} -> {self.author.username}'

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        unique_together = ['user', 'author']


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='liker',
        verbose_name='User',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='liked',
        verbose_name='Fast'
    )

    def __str__(self):
        return f'{self.user} -> {self.post}'

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = ['user', 'post']
