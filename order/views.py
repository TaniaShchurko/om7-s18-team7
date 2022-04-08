from django.shortcuts import render, redirect
from . import models
from authentication.models import CustomUser
from book.models import Book
from authentication.models import CustomUser
import datetime
from .forms import OrderForm
from django.shortcuts import get_object_or_404
# Create your views here.

def order_by_created_at(request):

    orders = list(models.Order.objects.all().order_by("created_at"))
    
    content = {
        'is_empty': not bool(orders),
        "orders": orders,
        'sorted_by': 'the data of creation',
    }
    return render(request, "order_sorted.html", content)


def order_by_plated_end_at(request):

    orders = list(models.Order.objects.all().order_by("plated_end_at"))
    
    content = {
        'is_empty': not bool(orders),
        "orders": orders,
        'sorted_by': 'the data of an order\'s ending',
    }
    return render(request, "order_sorted.html", content)

def order_from_specific_user(request, user_id):

    
    if CustomUser.get_by_id(user_id) is None:
        
        content = {
            'user_not_found' : True,
        }
        
        return render(request, 'order_user.html', content)


    orders = list(models.Order.objects.filter(user__in=CustomUser.objects.filter(id=user_id)))
    content = {
        'user_not_found': False,
        'user': CustomUser.get_by_id(user_id),
        'is_empty': not bool(orders),
        "orders": orders,
        'sorted_by': 'the data of an order\'s ending',

    }

    return render(request, 'order_user.html', content)


def over_dated_orders(request):

    orders = list(models.Order.objects.filter(plated_end_at__lte=datetime.datetime.now()))
    users_order = {order.user for order in orders}
    users = {}
    for user in users_order:
        users.update({user:[]})
    for order in orders:
        users[order.user].append(order)

    content = {
        'is_empty': not bool(users),
        'users' : users,
    }

    return render(request, 'over_dated.html', content)




def order_post(request, id=0):
    if request.method == 'POST': #POST method
        if id == 0: #Add user
            form = OrderForm(request.POST)
            button_submit = 'Add'
        else:
            form = OrderForm(request.POST, instance=get_object_or_404(models.Order,pk=id))
            button_submit = 'Submit'
        
        if form.is_valid():
            form.save()
            return redirect('order:order_list')

    else: #GET method
        if id == 0: #Add user
            form = OrderForm()
            button_submit = 'Add'
        else:
            form = OrderForm( instance=get_object_or_404(models.Order,pk=id))
            button_submit = 'Submit'

    context = {
        'form':form,
        'button_submit':button_submit,
    }
    return render(request, 'user_post.html', context)