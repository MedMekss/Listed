from django.urls import path
from .views import (IndexView, CategoryAddView,
                    StatisticsView)

app_name = 'todo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
    path('c/add', CategoryAddView.as_view(), name='category_create')
]
