from rest_framework import serializers

from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "book_title",
            "category",
            "get_absolute_url",
            "price",
            "number_of_pages",
            "language",
        )

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = (
            "id",
            "first_name",
            "last_name",
            "country_of_origin",
            "get_absolute_url",
            "get_image",
            "books",
        )