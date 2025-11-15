# core/urls.py

from django.urls import path
from .views import index_view

urlpatterns = [
    # La ruta '' corresponde a la raíz del sitio.
    # Cuando un usuario visite la página principal, se ejecutará 'index_view'.
    # Le damos el nombre 'index' para referenciarla fácilmente.
    path('', index_view, name='index'),
]