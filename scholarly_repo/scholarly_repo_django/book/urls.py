from django.urls import path, include

from book import views

urlpatterns = [
    path('alphabetical-books/', views.AlphabeticalBooksList.as_view()),
    path('alphabetical-authors/', views.AlphabeticalAuthorsList.as_view()),
    path('authors/search/', views.author_search),
    path('books/search/', views.book_search),
    path('books/<slug:author_slug>/<slug:book_slug>/', views.BookDetail.as_view()),
    path('books/<slug:author_slug>/', views.AuthorDetail.as_view()),
]