from django.urls import path
from .views import segundo_grado_view

urlpatterns = [
    path('', segundo_grado_view, name='segundo_grado'),
]