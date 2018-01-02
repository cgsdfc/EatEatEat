from django.urls import path, include
from .views import index
from .views import DishesListView, DishesDetailView
from .views import RestaurantsListView, RestaurantsDetailView
from .views import Signin

urlpatterns=[
        path('', index),
        path('dishes/', DishesListView.as_view(), name='dishes'),
        path('dishes/<int:pk>/', DishesDetailView.as_view(), name='dish-detail'),
        path('restaurants/', RestaurantsListView.as_view(), name='restaurants'),
        path('restaurants/<int:pk>', RestaurantsDetailView.as_view(), name='restaurant-detail'),
        path('signin/', Signin, name='signin'),

        ]

