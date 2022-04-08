from django.shortcuts import redirect, render
from . import models
from order.models import Order
from .forms import BookForm
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    return redirect('/book/')

def all_books(request):
    books = models.Book.get_all()

    context = {
        'is_empty' : not bool(books),
        'books' : books
    }

    return render(request, 'all_books.html', context)

def book_by_id(request, id_book):
    book = models.Book.get_by_id(id_book)
    context = {
        'not_found' : (book is None),
        'id' : id_book,
        'book' : book,
    }
    return render(request, 'book_by_id.html', context)


def filter_by_author_id(request, author_id):
    author = models.Author.get_by_id(author_id)

    if author is None:
        context = {
            'no_author': True,
            'author_id': author_id,
        }
    else:
        books = author.books.all()
        context = {
        'no_author' : False,
        'is_empty' : not bool(books),
        'books' : books,
        'author': author,
        }


    return render(request, 'filter_by_author_id.html', context)

def filter_by_part_of_name(request, part_of_name):

    books = list(models.Book.objects.filter(name__icontains=part_of_name))


    context = {
        'is_empty' : not bool(books),
        'books' : books,
        'part_of_name': part_of_name,
    }

    return render(request, 'filter_by_part_of_name.html', context)

def sort_by_name_desc(request):
    
    books = list(models.Book.objects.all().order_by('-name'))

    context = {
        'is_empty' : not bool(books),
        'books' : books,
        'sorted_by': 'name in descending order',
    }


    return render(request, 'all_sorted.html', context)

def sort_by_name_asc(request):
    
    books = list(models.Book.objects.all().order_by('name'))

    context = {
        'is_empty' : not bool(books),
        'books' : books,
        'sorted_by': 'name in ascending order',
    }


    return render(request, 'all_sorted.html', context)

def sort_by_count(request):
    
    books = list(models.Book.objects.order_by('count'))

    context = {
        'is_empty' : not bool(books),
        'books' : books,
        'sorted_by': 'count',
    }


    return render(request, 'all_sorted.html', context)

def all_unordered_books(request):

    ordered_books_id = {order.book.id for order in Order.objects.all()}
    books = list(models.Book.objects.exclude(id__in=ordered_books_id))
    print(ordered_books_id)
    context = {
        'is_empty' : not bool(books),
        'books' : books,
    }

    return render(request, 'unordered_books.html', context)


def book_post(request, id=0):

    if request.method == 'POST': #POST method
        if id==0: # Add book
            form=BookForm(request.POST)
            button_submit = 'Add'
        else:
            form=BookForm(request.POST, instance=get_object_or_404(models.Book,pk=id))
            button_submit = 'Update'

        if form.is_valid():
            form.save()
            return redirect('/book/')

    else: #GET method
        if id==0: # Add book
            form=BookForm()
            button_submit = 'Add'
        else:
            form=BookForm(instance=get_object_or_404(models.Book,pk=id))
            button_submit = 'Update'

    context = {
        'form':form,
        'button_submit': button_submit,

    }
    return render(request, 'book_post.html', context)