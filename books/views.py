from django.shortcuts import render,redirect
from .models import Book
from .forms import PostBook


# Create your views here.

def all_posts(request):
    context = dict()
    context['posts'] = Book.objects.all()

    return render(request=request, template_name="home.html", context=context)


def book_create_add(request):
    context = dict()

    form = PostBook(request.POST or None)

    if request.method == "POST":
        form = PostBook(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    context['form'] = form
    return render(request=request, template_name='book_form.html', context=context)