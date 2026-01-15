from django.urls import path
from . import views

urlpatterns = [
    path('', views.agradecimientos, name='agradecimientos'),
]