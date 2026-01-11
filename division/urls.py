# division/urls.py

from django.urls import path
from .views import division_view # Importa la función desde views.py

urlpatterns = [
    path('', division_view, name='division'),
]