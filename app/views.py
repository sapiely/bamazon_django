from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


def book_list(request):
    books = Book.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(books, 2)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    context = {'books': books}
    return render(request, 'books/index.html', context)


def book_info(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    authors = book.author.all()
    return render(request, 'books/detail.html', {'book': book, 'authors': authors})


def author_list(request):
    authors = Author.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(authors, 10)
    try:
        authors = paginator.page(page)
    except PageNotAnInteger:
        authors = paginator.page(1)
    except EmptyPage:
        authors = paginator.page(paginator.num_pages)
    context = {'authors': authors}
    return render(request, 'authors/index.html', context)


def author_info(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = get_list_or_404(Book, author=author_id)
    return render(request, 'authors/detail.html', {'author': author, 'books': books})


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
