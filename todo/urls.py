from django.urls import path
from .views import (IndexView, CategoryAddView,
                    StatisticsView, CheckListView)

app_name = 'todo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('statistics/', StatisticsView.as_view(), name='statistics'),
    path('c/<category_name>/', CheckListView.as_view(), name='checklist'),

    # path('c/add', CategoryAddView.as_view(), name='category_create')
]
