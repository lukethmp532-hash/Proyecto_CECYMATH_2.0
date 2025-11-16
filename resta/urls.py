from django.urls import path
from .views import resta_view

urlpatterns = [
    path('', resta_view, name='resta'),
]