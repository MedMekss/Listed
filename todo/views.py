from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, DetailView

from django.http import HttpResponse, JsonResponse
from . import forms
from . import models

import random


# /todo/
class IndexView(TemplateView):
    template_name = 'todo/index.html'


class CreateView(View):
    def get(self, request):
        context = {
            'category_form': forms.CategoryForm,
            'checklist_form': forms.ChecklistForm
        }
        return render(request=request, template_name='todo/create.html', context=context)


class StatisticsView(TemplateView):
    template_name = 'todo/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = models.Category.objects.all()
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

        best = models.Category.objects.first()
        best_percentage = 0
        worst = models.Category.objects.first()
        worst_percentage = 100

        for category in categories:
            items = []
            for checklist in models.CheckList.objects.filter(category=category):
                items += models.Item.objects.filter(checklist=checklist)
            items_count = 0
            items_checked = 0
            for item in items:
                items_count += 1
                if item.completed:
                    items_checked += 1
            try:
                percentage = int((items_checked / items_count) * 100)
            except:
                percentage = 0

            if percentage > best_percentage:
                best_percentage = percentage
                best = category
            if percentage < worst_percentage:
                worst_percentage = percentage
                worst = category

        messages = models.Messages.objects.all()
        message = random.choice(messages)

        context['message'] = str.format(
            message.message,
            good_title=best.category_name,
            bad_title=worst.category_name
        )

        return context


class CheckListView(TemplateView):
    template_name = 'todo/checklist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = kwargs['category_name']
        context['checklists'] = models.CheckList.objects.filter(category__category_name__iexact=kwargs['category_name'])
        context['items'] = models.Item.objects.all()
        return context


def addCategory(request):
    if request.is_ajax():
        category = forms.CategoryForm(request.POST)
        if category.is_valid():
            category = category.save()
            return JsonResponse({
                'message': f'successfully created {category.category_name}',
                'success': True,
                'id': category.id
            })
        else:
            return JsonResponse({
                'message': 'Category name already exists',
                'success': False
            })
    else:
        return JsonResponse({
            'message': 'invalid ajax response',
            'success': False
        })


def addChecklist(request):
    if request.is_ajax():
        checklist = forms.ChecklistForm(request.POST)
        if checklist.is_valid():
            checklist.save()
            return JsonResponse({
                'message': f'successfully created {checklist.cleaned_data["checklist_name"]}',
                'success': True
            })
        else:
            return JsonResponse({
                'message': 'Category name already exists',
                'success': False
            })
    else:
        return JsonResponse({
            'message': 'invalid ajax response',
            'success': False
        })


def checkGoal(request, id):
    goal = models.Item.objects.get(id=id)
    goal.completed = False if goal.completed else True
    goal.save()
    return JsonResponse({})
