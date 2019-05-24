from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, DetailView

from django.http import HttpResponse, JsonResponse
from . import forms
from . import models


# /todo/
class IndexView(TemplateView):
    template_name = 'todo/statistics.html'


class StatisticsView(TemplateView):
    template_name = 'todo/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = models.Category.objects.all()
        context['categories'] = categories
        context['category_sizes'] = [len(models.CheckList.objects.filter(category=category)) for category in categories]

        context['bar_data'] = []

        for category in categories:
            items = []
            for checklist in models.CheckList.objects.filter(category=category):
                items += models.Item.objects.filter(checklist=checklist)
            checked = 0
            for item in items:
                if item.completed:
                    checked += 1
            try:
                context['bar_data'].append(int((checked / len(items) * 100)))
            except:
                context['bar_data'].append(0)
        return context


class CheckListView(TemplateView):
    template_name = 'todo/checklist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = kwargs['category_name']
        context['checklists'] = models.CheckList.objects.filter(category__category_name__iexact=kwargs['category_name'])
        context['items'] = models.Item.objects.all()
        return context


class CategoryAddView(FormView):
    template_name = 'todo/statistics.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('todo:category_create')

    def form_valid(self, form):
        form.save()
        return super(CategoryAddView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CategoryAddView, self).get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context
