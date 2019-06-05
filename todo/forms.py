from django import forms
from django.forms import widgets
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'color']
        widgets = {
            'color': widgets.TextInput(attrs={'type': 'color', 'class': 'xddddd'}),
        }
