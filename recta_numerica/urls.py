# recta_numerica/urls.py

from django.urls import path
from .views import recta_numerica_view

urlpatterns = [
    path('', recta_numerica_view, name='recta_numerica'),
]