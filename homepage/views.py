from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish, Restaurant
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def index(request):
    dishes = Dish.objects.all()
    return render(request, 'homepage/cover.html', context={ 'dishes': dishes })

class DishesListView(ListView):
    paginate_by=10
    model=Dish

class DishesDetailView(DetailView):
    model=Dish

class RestaurantsListView(ListView):
    paginate_by=10
    model=Restaurant

class RestaurantsDetailView(DetailView):
    model=Restaurant

