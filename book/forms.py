from django import forms
from author.models import Author

class BookForm(forms.Form):
        name = forms.CharField(label="name", max_length=128)
        description = forms.CharField(label="description")
        count = forms.IntegerField(label="count")
        authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

class EditBookForm(forms.Form):
        name = forms.CharField(label="name", max_length=128,required=False)
        description = forms.CharField(label="description", required=False)
        count = forms.IntegerField(label="count", required=False)
        authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), required=False)