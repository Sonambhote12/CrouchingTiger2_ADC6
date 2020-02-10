from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('__all__')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }