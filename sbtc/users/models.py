from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(
        'about the author',
        max_length=500,
        blank=True,
        null=True,
        help_text='tell us about yourself'
    )
    location = models.CharField(
        'City',
        max_length=30,
        blank=True,
        null=True,
        help_text='Where do you live?'
    )
    birth_date = models.DateField(
        'Date of Birth',
        null=True,
        blank=True,
        help_text='Enter date of birth'
    )
    photo = models.ImageField(
        'Photo',
        upload_to='profile/',
        blank=True,
        help_text='Attach your photo',
    )

    def __str__(self):
        return f'User profile: {self.user.username}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
