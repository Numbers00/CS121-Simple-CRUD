from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class AlphabeticalAuthorsList(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()[0:99]
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        authors = Author.objects.all()
        authors.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            country_of_origin=request.data['country_of_origin'],
            image=request.data['image'],
            slug=request.data['slug']
        )
        return Response({"Authors": []})

class AlphabeticalBooksList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        targetAuthor = Author.objects.filter(Q(first_name=request.data['author_first_name']))
        books = Book.objects.all()
        books.create(
            author=targetAuthor[0], 
            book_title=request.data['book_title'], 
            category=request.data['category'], 
            price=request.data['price'],
            number_of_pages=request.data['number_of_pages'],
            language=request.data['language'],
            slug=request.data['slug']
        )
        return Response({"Books": []})

class BookDetail(APIView):
    def get_object(self, author_slug, book_slug):
        try:
            return Author.objects.filter(author__slug=author_slug).get(slug=book_slug)
        except Book.DoesNotExist:
            raise Http404
    
    def get(self, request, author_slug, book_slug, format=None):
        book = self.get_object(author_slug, book_slug)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class AuthorDetail(APIView):
    def get_object(self, author_slug):
        try:
            return Author.objects.get(slug=author_slug)
        except Author.DoesNotExist:
            raise Http404
    
    def get(self, request, author_slug, format=None):
        author = self.get_object(author_slug)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

@api_view(['POST'])
def author_search(request):
    query = request.data.get('query', '')

    if query:
        authors = Author.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    else:
        return Response({"Authors": []})

@api_view(['POST'])
def book_search(request):
    query = request.data.get('query', '')

    if query:
        books = Book.objects.filter(Q(book_title__icontains=query))
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response({"Books": []})