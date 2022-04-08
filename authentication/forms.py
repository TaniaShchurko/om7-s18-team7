from django import forms
from .models import CustomUser
from datetime import datetime
import pytz

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','middle_name','last_name', 'email']

    
    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True

    
    