from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from django.http import HttpResponse, JsonResponse
from . import forms
from . import models


# /todo/
<<<<<<< HEAD
class IndexView(TemplateView):
    template_name = 'todo/index.html'
=======
class IndexView(View):
    def get(self, request):
        context = {
            'category_form': forms.CategoryForm,
            'checklist_form': forms.ChecklistForm
        }
        return render(request=request, template_name='todo/create.html', context=context)
>>>>>>> origin/branch_jared

class CreateView(FormView):
    template_name = 'todo/create.html'

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


def addCategory(request):
    if request.method == "POST":
        category = forms.CategoryForm(request.POST)
        category.save()
    return redirect('/todo/')


def addChecklist(request):
    if request.method == "POST":
        checklist = forms.ChecklistForm(request.POST)
        checklist.save()
    return redirect('/todo/')
