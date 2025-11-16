# factorizacion/urls.py

from django.urls import path
from .views import factorizacion_view

urlpatterns = [
    path('', factorizacion_view, name='factorizacion'),
]