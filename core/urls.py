# core/urls.py

from django.urls import path
from .views import index_view

urlpatterns = [
    # La ruta '' corresponde a la raíz del sitio.
    path('', index_view, name='index'),
]