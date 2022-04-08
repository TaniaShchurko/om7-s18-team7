from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(label='name',max_length=20)
    surname = forms.CharField(label='surname', max_length=20)
    patronymic = forms.CharField(label='patronymic', max_length=20)

class EditAuthorForm(forms.Form):
    name = forms.CharField(label='name', max_length=20, required=False)
    surname = forms.CharField(label='surname', max_length=20, required=False)
    patronymic = forms.CharField(label='patronymic', max_length=20, required=False)