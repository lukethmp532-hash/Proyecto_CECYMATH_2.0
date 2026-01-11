from django.urls import path
from . import views

urlpatterns = [
    path('', views.ecuaciones_segundo_grado, name='ecuaciones_segundo_grado'),
]