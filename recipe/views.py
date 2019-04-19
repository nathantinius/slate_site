from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe

def home(request):
    recipes = Recipe.objects
    return render(request, 'recipe/home.html', {'recipes': recipes})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['inputRecipeName'] and request.FILES['inputRecipeImage']:
            recipe = Recipe()
            recipe.name = request.POST['inputRecipeName']
            recipe.image = request.FILES['inputRecipeImage']
            recipe.save()
            return redirect('home')
        else:
            return render(request, 'recipe/create.html', {'error', 'All fields are required.'})
    else:
        return render(request, 'recipe/create.html')

    return render(request, 'recipe/create.html')
