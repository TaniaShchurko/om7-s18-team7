from django import forms
from .models import Order
from datetime import datetime, timedelta

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'book', 'plated_end_at', 'end_at']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['plated_end_at'].initial = datetime.now()+timedelta(days=15)
        self.fields['end_at'].required = False
        self.fields['user'].label_from_instance = lambda user: f'{user.first_name} {user.middle_name} {user.last_name}'
        self.fields['book'].label_from_instance = lambda book: f'{book.name} ( {book.description[:16]}...)'