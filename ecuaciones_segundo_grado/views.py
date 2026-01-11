# ecuaciones_segundo_grado/views.py

from django.shortcuts import render
import math # Importamos la librería math para la raíz cuadrada

def ecuaciones_segundo_grado(request):
    resultado = None
    error = None
    valores_originales = {}

    if request.method == 'POST':
        try:
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            c = float(request.POST.get('c'))
            valores_originales = {'a': a, 'b': b, 'c': c}

            if a == 0:
                error = "El coeficiente 'a' no puede ser cero en una ecuación de segundo grado."
            else:
                # Calculamos el discriminante: b^2 - 4ac
                discriminante = (b**2) - (4 * a * c)

                if discriminante > 0:
                    # Dos soluciones reales y distintas
                    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
                    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
                    resultado = f"La ecuación tiene dos soluciones reales: x₁ = {x1:.4f} y x₂ = {x2:.4f}"
                elif discriminante == 0:
                    # Una única solución real
                    x = -b / (2 * a)
                    resultado = f"La ecuación tiene una única solución real: x = {x:.4f}"
                else:
                    # No hay soluciones reales
                    resultado = "La ecuación no tiene soluciones en los números reales (el discriminante es negativo)."

        except (ValueError, TypeError):
            error = "Por favor, introduce coeficientes numéricos válidos."

    contexto = {
        'resultado': resultado,
        'error': error,
        'v': valores_originales
    }
    return render(request, 'ecuaciones_segundo_grado/segundo_grado.html', contexto)