from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm
from .models import Author


# Create your views here.

def authors_update(request, id=0):

    if request.method == 'POST': #Post method
        if id == 0:
            form = AuthorForm(request.POST)
            button_submit = 'Add'
        else:
            form = AuthorForm(request.POST, instance=get_object_or_404(Author,pk=id))
            button_submit = 'Update'

        if form.is_valid():
            form.save()
            return redirect('/author/list')

    else: #Get method
        if id == 0:
            form = AuthorForm()
            button_submit = 'Add'
        else:
            form = AuthorForm(instance=get_object_or_404(Author,pk=id))
            button_submit = 'Update'
    content = {
        'form': form,
        'button_submit':button_submit
        }
    return render(request, 'add_author.html', content)


def author_list(request):
    authors = list(Author.objects.all())    
    context = {
        'is_empty': bool(authors),
        'authors': authors
    }

    return render(request, 'author_list.html', context)