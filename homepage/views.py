from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish, Restaurant
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def index(request):
    dishes = Dish.objects.all()
    return render(request, 'homepage/index.html', context={ 'dishes': dishes })

class DishesListView(ListView):
    model=Dish

class DishesDetailView(DetailView):
    model=Dish

class RestaurantsListView(ListView):
    model=Restaurant

class RestaurantsDetailView(DetailView):
    model=Restaurant

