from django.shortcuts import render

from .models import Recipe

def home(request):
    recipes = Recipe.objects
    return render(request, 'recipe/home.html', {'recipes': recipes})
