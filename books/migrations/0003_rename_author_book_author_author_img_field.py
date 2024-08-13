# Generated by Django 5.1 on 2024-08-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_remove_book_author_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Author',
            new_name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='img_field',
            field=models.ImageField(blank=True, null=True, upload_to='post-images/', verbose_name='Image'),
        ),
    ]
