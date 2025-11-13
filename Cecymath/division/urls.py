# division/urls.py

from django.urls import path
from .views import division_view # Importa la función desde views.py

urlpatterns = [
    # El path '' corresponde a la raíz de la app, en este caso '/division/'.
    # Llama a la función 'division_view' y le damos el nombre 'division'
    # para usarlo en los links del HTML.
    path('', division_view, name='division'),
]