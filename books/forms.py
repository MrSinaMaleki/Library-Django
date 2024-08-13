from django import forms
from .models import Book,Author


class PostBook(forms.ModelForm):
    class Meta:
        model = Book
        # fields = ["title", "author", "isbn"]
        exclude = ["date_published", "date_edited"]
        # widgets = {
        #     "title": forms.TextInput(attrs={"class": "form__field"}),
        #     "author": forms.TextInput(attrs={"class": "form__field"}),
        #     "isbn": forms.TextInput(attrs={"class": "form__field"})
        # }


class CreateAuthor(forms.ModelForm):
    class Meta:
        model = Author
        # fields = ["title", "author", "isbn"]
        exclude = ["books_count"]
        # widgets = {
        #     "title": forms.TextInput(attrs={"class": "form__field"}),
        #     "author": forms.TextInput(attrs={"class": "form__field"}),
        #     "isbn": forms.TextInput(attrs={"class": "form__field"})
        # }
