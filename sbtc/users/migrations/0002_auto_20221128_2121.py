# Generated by Django 3.2 on 2022-11-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, help_text='tell us about yourself', max_length=500, null=True, verbose_name='about the author'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, help_text='Where do you live?', max_length=30, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, help_text='Attach your photo', null=True, upload_to='profile/', verbose_name='Photo'),
        ),
    ]
