from django.urls import path
from .views import multiplicacion_view

urlpatterns = [
    path('', multiplicacion_view, name='multiplicacion'),
]