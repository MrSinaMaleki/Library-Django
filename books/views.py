from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import PostBook, CreateAuthor


# Create your views here.

def all_posts(request):
    context = dict()
    books = Book.objects.all()
    context['posts'] = books

    return render(request=request, template_name="home.html", context=context)


def book_create_add(request, book_id: int = 0):
    if book_id != 0:
        obj = get_object_or_404(Book, id=book_id)

        form = PostBook(request.POST or None, instance=obj)
        context = dict()
        # save the data from the form and
        # redirect to detail_view
        if form.is_valid():
            form.save()
            return redirect('home')

        # add form dictionary to context
        context["form"] = form

        return render(request, "book_form.html", context)

    context = dict()

    form = PostBook(request.POST or None)

    if request.method == "POST":
        form = PostBook(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    context['form'] = form
    return render(request=request, template_name='book_form.html', context=context)


def book_detail(request, book_id: int):
    context = dict()
    context['book'] = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', context)


def book_delete(request, book_id):
    obj = get_object_or_404(Book, id=book_id)

    obj.delete()
    print("post was deleted!")
    return redirect('home')


def add_author(request):
    context = dict()
    form = CreateAuthor(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')

    context['form'] = form
    return render(request=request, template_name='auther_add.html', context=context)
