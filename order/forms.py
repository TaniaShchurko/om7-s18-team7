from django import forms
from book.models import Book
from authentication.models import CustomUser


class OrderForm(forms.Form):
        user = forms.ModelChoiceField(label='user', queryset=CustomUser.objects.all())
        book = forms.ModelChoiceField(label='book', queryset=Book.objects.all())
        plated_end_at = forms.DateTimeField(label="count",
                                            widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))


class EditOrderForm(forms.Form):
        plated_end_at = forms.DateTimeField(label="count", required=False,
                                            widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))
        end_at = forms.DateTimeField(label="count", required=False,
                                     widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))
