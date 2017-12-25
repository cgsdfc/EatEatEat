from django.urls import path, include
from .views import index
from .views import DishesListView

urlpatterns=[
        path('', index),
        path('dishes/', DishesListView.as_view(), name='dishes'),
        ]

