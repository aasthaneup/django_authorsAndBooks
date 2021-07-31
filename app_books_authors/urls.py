from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('add_book', views.add_books),
    path('add_author', views.add_authors),
    path('one_author/<int:id>', views.one_author),
    path('one_book/<int:id>', views.one_book),
    path('add_book_to_author/<int:id>', views.add_book_to_author),
    path('add_author_to_book/<int:id>', views.add_author_to_book)
    
]