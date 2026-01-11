"""
URL configuration for Cecymath project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),

    path('suma/', include('suma.urls')),
    
    path('resta/', include('resta.urls')),

    path('multiplicacion/', include('multiplicacion.urls')),

    path('polinomios/', include('polinomios.urls')),

    path('ecuaciones_primer_grado/', include('ecuaciones_primer_grado.urls')),

    path('ecuaciones_segundo_grado/', include('ecuaciones_segundo_grado.urls')),

    path('factorizacion/', include('factorizacion.urls')),

    path('areas-perimetros/', include('areas_perimetros.urls')),

    path('division/', include('division.urls')),

    path('jerarquia/', include('jerarquia.urls')),

    # Cuando alguien visite "/recta-numerica/", Django buscará las URLs en la app "recta_numerica".
    path('recta-numerica/', include('recta_numerica.urls')),
]
