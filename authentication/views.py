from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . models import CustomUser
from order.models import *
from . forms import EditCustomUserForm,CustomUserForm
from rest_framework import generics
from .serializers import UserDetailSerializer, UserListSerializer

# Create your views here.


def main(request):
    return render(request, 'authentication/layout.html')


def books_from_user(request):
    orders = Order.get_all()
    users_books = []
    contex = {
        "users_not_in_time": users_books
    }
    for order in orders:
        if order.created_at >= order.plated_end_at:
            users_books.append(order)
    print(users_books)
    return render(request, 'authentication/not_on_time.html', contex)


def all_user(request, id=None, way=None):
    if id:
        user = CustomUser.objects.get(id=id)
        user_books = Order.objects.filter(user=id)
        context = {
            "orders_by_user": user_books,
            "user": user
        }
        return render(request, "authentication/users_list.html", context)
    else:
        if way:
            users = CustomUser.objects.all().order_by(way)
            context = {
                "all_users": users
            }
            return render(request, "authentication/users_list.html", context)

        else:
            users = CustomUser.objects.all().order_by("first_name")
            context = {
                "all_users": users
            }
            return render(request, "authentication/users_list.html", context)


def add_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            CustomUser.create(email=form.cleaned_data['email'],
                              password=form.cleaned_data['email'],
                              first_name=form.cleaned_data['first_name'],
                              middle_name=form.cleaned_data['middle_name'],
                              last_name=form.cleaned_data['last_name'])
            return HttpResponseRedirect('/all_users/')
    else:
        form = CustomUserForm()

    return render(request, 'authentication/form.html', {'form': form})


def edit_user(request, id):
    if request.method == 'POST':
        form = EditCustomUserForm(request.POST)
        user = CustomUser.get_by_id(id)
        if form.is_valid():
            user.update(password=form.cleaned_data['password'],
                        first_name=form.cleaned_data['first_name'],
                        middle_name=form.cleaned_data['middle_name'],
                        last_name=form.cleaned_data['last_name'])
            return HttpResponseRedirect('/all_users/')
    else:
        form = EditCustomUserForm()

    return render(request, 'authentication/edit.html', {'form': form, 'id': id})


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = CustomUser.get_all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = CustomUser.get_all()