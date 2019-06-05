from django.urls import path
from .views import (IndexView, StatisticsView,
                    CheckListView)

app_name = 'todo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
    path('c/<category_name>/', CheckListView.as_view(), name='checklist'),
]
