from django import forms


class CustomUserForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=128)
    first_name = forms.CharField(label='Fist name', max_length=20)
    middle_name = forms.CharField(label='Middle name', max_length=20)
    last_name = forms.CharField(label='Last name', max_length=20)


class EditCustomUserForm(forms.Form):
    password = forms.CharField(label='Password', max_length=128, required=False)
    first_name = forms.CharField(label='Fist name', max_length=20, required=False)
    middle_name = forms.CharField(label='Middle name', max_length=20, required=False)
    last_name = forms.CharField(label='Last name', max_length=20, required=False)

