# core/views.py
from django.shortcuts import render

def index_view(request):
    """
    Esta vista se encarga de renderizar la página de inicio del proyecto,
    que funcionará como el menú principal.
    """
    return render(request, 'core/index.html')