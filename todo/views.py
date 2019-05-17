from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from django.http import HttpResponse, JsonResponse
from . import forms
from . import models


# /todo/
class IndexView(TemplateView):
    template_name = 'todo/statistics.html'


class CategoryAddView(FormView):
    template_name = 'todo/template.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('todo:category_create')

    def form_valid(self, form):
        form.save()
        return super(CategoryAddView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CategoryAddView, self).get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context
