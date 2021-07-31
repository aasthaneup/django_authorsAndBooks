from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        'all_books' : Book.objects.all()
    }
    return render(request, 'index.html', context)

def authors(request):
    context = {
        'all_authors' : Author.objects.all()
    }
    return render(request, 'authors.html', context)

def one_book(request, id):
    context = {
        "book" : Book.objects.get(id = id),
        'all_authors' : Author.objects.all()
    }
    return render(request, 'one_book.html', context)

def one_author(request, id):
    context = {
        'author' : Author.objects.get(id = id),
        'all_books' : Book.objects.all()
    }
    return render(request, 'one_author.html', context)

def add_books(request):
    Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/')

def add_authors(request):
    Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])
    return redirect('/authors')

def add_author_to_book(request, id):
    this_author = Author.objects.get(id = request.POST['author_to_add'])
    this_book = Book.objects.get(id = id)
    this_author.books.add(this_book)

    return redirect(f'/one_book/{id}')

def add_book_to_author(request, id):
    this_author = Author.objects.get(id = id)
    this_book = Book.objects.get(id = request.POST['book_to_add'])
    this_author.books.add(this_book)

    return redirect(f'/one_author/{id}')