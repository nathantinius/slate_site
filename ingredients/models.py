from django.db import models

class Ingredients(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE,)

    
