# jerarquia/urls.py

from django.urls import path
from .views import jerarquia_view  # Importamos la vista que creamos

urlpatterns = [
    # Cuando un usuario vaya a la URL '/jerarquia/', se ejecutará la función 'jerarquia_view'.
    # Le damos el nombre 'jerarquia' para poder llamarla fácilmente desde el HTML.
    path('', jerarquia_view, name='jerarquia'),
]