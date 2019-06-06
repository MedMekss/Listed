from django.urls import path
from .views import *

app_name = 'todo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('c/add', CategoryAddView.as_view(), name='category_create'),
    path('addCategory/', addCategory, name='addCategory'),
    path('addChecklist/', addChecklist, name='addChecklist'),
    path('create/', addChecklist, name='create')
]
