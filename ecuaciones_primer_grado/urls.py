# ecuaciones_primer_grado/urls.py

from django.urls import path
from .views import primer_grado_view

urlpatterns = [
    path('', primer_grado_view, name='ecuaciones_primer_grado'),
]