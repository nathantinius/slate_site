from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:recipe_id>', views.detail, name='detail' ),
]
