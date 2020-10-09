from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Book, Author


def book_list(request):
    latest_books_list = Book.objects.order_by('-release_date')[:5]
    context = {'latest_books_list': latest_books_list}
    return render(request, 'books/index.html', context)


def book_info(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    authors = book.author.all()
    return render(request, 'books/detail.html', {'book': book, 'authors': authors})


def author_info(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'authors/detail.html', {'author': author})



