from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Ingredients(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey('recipe.Recipe', verbose_name=_('recipe'), related_name='ingredients', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
