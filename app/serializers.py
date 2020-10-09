from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("author", "title", "description", "release_date")


class BookForAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("author", "title")


class AuthorSerializer(serializers.ModelSerializer):
    book_list = BookForAuthorsSerializer(many=True, read_only=True, source="author")

    class Meta:
        model = Author
        fields = (
            "id",
            "full_name",
            "description",
            "birth_date",
            "death_date",
            "book_list",
        )
