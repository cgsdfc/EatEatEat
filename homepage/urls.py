from django.urls import path, include
from .views import index
from .views import DishesListView, DishesDetailView
from .views import RestaurantsListView, RestaurantsDetailView
from .views import Signin, LearnMore, About

urlpatterns=[
        path('', index, name='homepage'),
        path('dishes/', DishesListView.as_view(), name='dishes'),
        path('dishes/<int:pk>/', DishesDetailView.as_view(), name='dish-detail'),
        path('restaurants/', RestaurantsListView.as_view(), name='restaurants'),
        path('restaurants/<int:pk>', RestaurantsDetailView.as_view(), name='restaurant-detail'),
        path('signin/', Signin, name='signin'),
        path('learn_more/', LearnMore, name='learn_more'),
        path('about/', About, name='about'),
        ]

