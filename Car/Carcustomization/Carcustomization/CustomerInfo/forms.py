from django import forms

from .models import DesireInfo


class OrderForm(forms.ModelForm):
    class Meta:
        model = DesireInfo
        fields = ('CustomerName', 'CarName', 'pdf', 'cover')
        