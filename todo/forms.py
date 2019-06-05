from django import forms
from django.forms import widgets
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'color']
        widgets = {
            'category_name': forms.TextInput(attrs={'placeholder': 'Enter Category Name', 'class': 'textinput no-border transpearant'}),
            'color': forms.TextInput(attrs={'type':'color', 'class':'nopad transpearant no-border', 'style':'margin-top: 4px'})
        }
        labels = {'Choose Color'}


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = CheckList
        fields = ['checklist_name', 'category', 'start_date', 'end_date']
        widgets = {
            'checklist_name': forms.TextInput(attrs={'placeholder': 'Enter Checklist Name', 'class': 'no-border transpearant'}),
            'category':forms.Select(attrs={'class':''}),
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'end_date': forms.TextInput(attrs={'type': 'date'})
        }
