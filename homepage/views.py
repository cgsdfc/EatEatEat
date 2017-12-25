from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish, Restaurant

def index(request):
    dishes = Dish.objects.all()
    print(dishes)
    return render(request, 'homepage/index.html', context={ 'dishes': dishes })


