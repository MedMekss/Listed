from django.urls import path
from .views import (IndexView, CategoryAddView)

app_name = 'todo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('c/add', CategoryAddView.as_view(), name='category_create')
]
