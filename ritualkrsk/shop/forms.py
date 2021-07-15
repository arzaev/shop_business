from django import forms
from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'surname', 'address', 'email', 'phone')
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'address': 'Адрес',
            'email': 'Email',
            'phone': 'Телефон',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-md-12 form-control'}),
            'surname': forms.TextInput(attrs={'class': 'col-md-12 form-control'}),
            'address': forms.TextInput(attrs={'class': 'col-md-12 form-control'}),
            'email': forms.EmailInput(attrs={'class': 'col-md-12 form-control'}),
            'phone': forms.TextInput(attrs={'class': 'col-md-12 form-control'}),

        }
