# areas_perimetros/urls.py

from django.urls import path
from .views import areas_perimetros_view

urlpatterns = [
    path('', areas_perimetros_view, name='areas_perimetros'),
]