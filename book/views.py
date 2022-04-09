from django.shortcuts import render
from . models import Book
from .forms import BookForm, EditBookForm
from order.models import Order
from rest_framework import generics
from book.serializer import BookDetailSerializer, BookListSerializer
from django.http import HttpResponseRedirect
# Create your views here.


def books(request):
    books = Book.objects.order_by('name')
    return render(request, 'book/allbooks.html', {'books': books})


def book_by_id(request, id):
    book = Book.get_by_id(id)
    return render(request, 'book/book_by_id.html', {'book': book})


def books_name_desc(request):
    books = Book.objects.order_by('-name')
    return render(request, 'book/allbooks.html', {'books': books})


def books_count(request):
    books = Book.objects.order_by('count')
    return render(request, 'book/allbooks.html', {'books': books})


def unordered(request):
    books = Book.get_all()
    unordered = []
    for book in books:
        if not Order.objects.filter(book=book):
            unordered.append(book)
    return render(request, 'book/allbooks.html', {'books': unordered})

def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.create(name=form.cleaned_data['name'],
                        description=form.cleaned_data['description'],
                        count=form.cleaned_data['count'],
                        authors=form.cleaned_data['authors'])
            return HttpResponseRedirect('/book/books')
    else:
        form = BookForm()

    return render(request, 'book/adding.html', {'form': form})

def edit(request,id):
    if request.method == 'POST':
        form = EditBookForm(request.POST)
        book = Book.get_by_id(id)
        if form.is_valid():
            book.update(name=form.cleaned_data['name'],
                        description=form.cleaned_data['description'],
                        count=form.cleaned_data['count'],
                        authors=form.cleaned_data['authors'])
            return HttpResponseRedirect('/book/books')
    else:
        form = EditBookForm()

    return render(request, 'book/edit.html', {'form': form})

class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer


class BookListView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()