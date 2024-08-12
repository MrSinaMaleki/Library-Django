from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    author = models.CharField(max_length=200, verbose_name="author")

    isbn = models.CharField(max_length=13, verbose_name="Shabak Serial")

    date_published = models.DateTimeField(auto_now_add=True, db_index=True)
    date_edited = models.DateTimeField(null=True, auto_now=True)
