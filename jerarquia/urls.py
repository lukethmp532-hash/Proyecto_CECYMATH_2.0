# jerarquia/urls.py

from django.urls import path
from .views import jerarquia_view  # Importamos la vista que creamos

urlpatterns = [
    path('', jerarquia_view, name='jerarquia'),
]