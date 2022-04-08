from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from .forms import CustomUserForm

# Create your views here.


def user_list(request):
    users = list(CustomUser.get_all())
    context = {
        'is_empty': not bool(users),
        'users': users,
    }

    return render(request, 'user_list.html', context)

def user_post(request, id=0):
    if request.method == 'POST': #POST method
        if id == 0: #Add user
            form = CustomUserForm(request.POST)
            button_submit = 'Add'
        else:
            form = CustomUserForm(request.POST, instance=get_object_or_404(CustomUser,pk=id))
            button_submit = 'Submit'
        
        if form.is_valid():
            form.save()
            return redirect('user:user_list')

    else: #GET method
        if id == 0: #Add user
            form = CustomUserForm()
            button_submit = 'Add'
        else:
            form = CustomUserForm( instance=get_object_or_404(CustomUser,pk=id))
            button_submit = 'Submit'

    context = {
        'form':form,
        'button_submit':button_submit,
    }
    return render(request, 'user_post.html', context)