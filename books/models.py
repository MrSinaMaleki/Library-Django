from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    books_count = models.PositiveIntegerField(null=True)

    img_field = models.ImageField(verbose_name="Image", upload_to='post-images/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    # author = models.CharField(max_length=200, verbose_name="author")

    isbn = models.CharField(max_length=13, verbose_name="Shabak Serial")

    date_published = models.DateTimeField(auto_now_add=True, db_index=True)
    date_edited = models.DateTimeField(null=True, auto_now=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
