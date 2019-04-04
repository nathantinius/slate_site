from django.db import models

class Recipe(models.Model):
    name=models.CharField(max_length=150)
    image=models.ImageField(upload_to='images/')
    created=models.DateField(auto_now_add=True)
