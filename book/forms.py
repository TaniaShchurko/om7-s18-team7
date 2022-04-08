from django import forms
from .models import Book
from author.models import Author

from django.forms import fields

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count','authors']
    
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple(),

    )
    

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['authors'].label_from_instance = lambda obj : f'{obj.surname} {obj.name} {obj.patronymic}'