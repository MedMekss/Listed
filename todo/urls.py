from django.urls import path
from .views import *

app_name = 'todo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
    path('c/<category_name>/', CheckListView.as_view(), name='checklist'),

    path('create/', CreateView.as_view(), name='create'),
    path('addCategory/', addCategory, name='addCategory'),
    path('addChecklist/', addChecklist, name='addChecklist'),
    path('checkGoal/<id>', checkGoal, name='checkGoals'),
]
