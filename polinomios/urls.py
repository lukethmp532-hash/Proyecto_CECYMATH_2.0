# polinomios/urls.py

from django.urls import path
from .views import polinomios_view

urlpatterns = [
    path('', polinomios_view, name='polinomios'),
]