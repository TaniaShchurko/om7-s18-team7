import datetime

import pytz
from django.http import HttpResponse, HttpResponseRedirect
from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from .forms import OrderForm, EditOrderForm

from django.shortcuts import render
from . models import Order
from rest_framework import generics
from .serializers import OrderDetailSerializer, OrderListSerializer

# Create your views here.


def orders(request):
    orders = Order.objects.order_by('created_at').order_by('plated_end_at')
    return render(request, 'order/orders_sorted_by_date.html', {'orders': orders})


def db(request):
    TEST_DATE = datetime.datetime(2017, 4, 10, 12, 00, tzinfo=pytz.utc)
    TEST_DATE_END = TEST_DATE + datetime.timedelta(days=15)

    user = CustomUser(id=111, email='email@mail.com', password='1234', first_name='fname',
                      middle_name='mname',
                      last_name='lname')
    user.save()
    user_free = CustomUser(id=222, email='2email@mail.com', password='1234', first_name='2fname',
                           middle_name='2mname',
                           last_name='2lname')
    user_free.save()
    author1 = Author(id=101, name="author1", surname="s1", patronymic="p1")
    author1.save()

    author2 = Author(id=102, name="author2", surname="s2", patronymic="p2")
    author2.save()

    book1 = Book(id=101, name="book1", description="description1", count=1)
    book1.save()
    book1.authors.add(author1)
    book1.save()

    book2 = Book(id=102, name="book2", description="description2")
    book2.save()
    book2.authors.add(author2)
    book2.save()

    book3 = Book(id=103, name="book3", description="description3")
    book3.save()
    book3.authors.add(author1)
    book3.authors.add(author2)
    book3.save()

    order1 = Order(id=101, user=user, book=book1, plated_end_at=TEST_DATE)
    order1.save()
    order2 = Order(id=102, user=user, book=book2, plated_end_at=TEST_DATE)
    order2.save()
    order3 = Order(id=103, user=user, book=book3, end_at=TEST_DATE_END, plated_end_at=TEST_DATE)
    order3.save()
    return HttpResponse("db set")


def addOrder(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.create(user=form.cleaned_data['user'],
                         book=form.cleaned_data['book'],
                         plated_end_at=form.cleaned_data['plated_end_at'])
            return HttpResponseRedirect('/order/orders/')
    else:
        form = OrderForm()

    return render(request, 'order/new_order.html', {'form': form})


def editOrder(request, id):
    if request.method == 'POST':
        form = EditOrderForm(request.POST)
        order = Order.get_by_id(id)
        if form.is_valid():
            order.update(plated_end_at=form.cleaned_data['plated_end_at'],
                         end_at=form.cleaned_data['end_at'])
            return HttpResponseRedirect('/order/orders/')
    else:
        form = EditOrderForm()

    return render(request, 'order/edit.html', {'form': form, 'id': id})


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    