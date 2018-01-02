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

def Signin(request):
    return render(request, 'homepage/signin.html', context={})

def About(request):
    return render(request, 'homepage/about.html', context={})

def LearnMore(request):
    dish_list=Dish.objects.all()
    restaurant_list=Restaurant.objects.all()
    return render(request, 'homepage/learn_more.html', context={
        'dish_list':dish_list,
        'restaurant_list':restaurant_list,
        })
