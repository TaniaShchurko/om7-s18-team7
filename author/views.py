from django.shortcuts import render, redirect
from author.models import *
from django.http import HttpResponseRedirect
from rest_framework import generics
from author.serializer import AuthorDetailSerializer, AuthorListSerializer
from .forms import AuthorForm, EditAuthorForm
from book.models import *

# def author_id_books(request):
#     #all_authors = Author.objects.order_by("?")[0]         # random select one author
#     all_authors = Author.objects.all()
#     context = {
#         "authors": all_authors
#     }
#     return render(request, "author/all_books_by_author.html", context)


def add_author(request):
    for i in range(10):
        Author.create(name="n" + str(i), surname="sur" + str(i), patronymic="p" + str(i))
    # author = Author.objects.all()          # delete all authors
    # author.delete()
    return redirect("books")


def books_from_author(request, id):
    books = Book.get_all()
    authors_books = []
    for book in books:
        if book.author.all().filter(id=id):
            authors_books.append(book)
    return render(request, 'book/allbooks.html', {'books': authors_books})

def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            Author.create(name=form.cleaned_data['name'],
                        surname=form.cleaned_data['surname'],
                        patronymic=form.cleaned_data['patronymic'])
            return HttpResponseRedirect('all_users/')
    else:
        form = AuthorForm()
    return render(request, 'author/add_author.html', {'form': form})

def editauthor(request, id):
    if request.method == 'POST':
        form = EditAuthorForm(request.POST)
        author = Author.get_by_id(id)
        if form.is_valid():
            author.update(name=form.cleaned_data['name'],
                        surname=form.cleaned_data['surname'],
                        patronymic=form.cleaned_data['patronymic'])
            return HttpResponseRedirect('/all_users/')
    else:
        form = EditAuthorForm()

    return render(request, 'author/edit.html', {'form': form, 'id': id})

def authors(request):
    author = Author.objects.order_by('name')
    return render(request, 'author/allauthors.html', {'authors': author})

class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorDetailSerializer

class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorListSerializer
    queryset = Book.objects.all()

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorDetailSerializer
    queryset = Book.objects.all()
