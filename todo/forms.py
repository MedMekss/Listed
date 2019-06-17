from django import forms
from django.forms import widgets
from .models import CheckList, Category, Item


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'color']
        widgets = {
            'category_name': forms.TextInput(attrs={'placeholder': 'Enter Category Name', 'class': 'overflowscroll w-100 textinput no-border transpearant'}),
            'color': forms.TextInput(attrs={'type':'color', 'class':'nopad transpearant no-border', 'style':'margin-left: 8px; margin-bottom:6px'})
        }
        labels = {'Choose Color'}


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = CheckList
        fields = ['checklist_name', 'category', 'start_date', 'end_date']
        widgets = {
            'checklist_name': forms.TextInput(attrs={'placeholder': 'Enter Checklist Name', 'class': 'overflowscroll w-100 no-border transpearant'}),
            'category':forms.Select(attrs={'class':'', 'style': 'margin-left:10px' }),
            'start_date': forms.TextInput(attrs={'type': 'date', 'style': 'margin-left:4px', 'min':{}}),
            'end_date': forms.TextInput(attrs={'type': 'date', 'style': 'margin-left:10px; padding-right:2px; margin-top:10px'})
        }