# factorizacion/views.py

from django.shortcuts import render
import math

def factorizacion_view(request):
    resultado = None
    error = None
    valores_originales = {}

    if request.method == 'POST':
        try:
            b = int(request.POST.get('b'))
            c = int(request.POST.get('c'))
            valores_originales = {'b': b, 'c': c}

            # Lógica para encontrar dos números que sumen 'b' y multipliquen 'c'
            encontrado = False
            # Solo buscamos factores hasta la raíz cuadrada de |c| para ser eficientes
            for i in range(1, int(math.sqrt(abs(c))) + 1):
                if c % i == 0:
                    j = c // i
                    # Comprobamos las 4 combinaciones posibles de signos
                    if i + j == b:
                        resultado = f"(x + {i})(x + {j})"
                        encontrado = True
                        break
                    if -i + -j == b:
                        resultado = f"(x - {i})(x - {j})"
                        encontrado = True
                        break
                    if i + -j == b:
                        resultado = f"(x + {i})(x - {j})"
                        encontrado = True
                        break
                    if -i + j == b:
                        resultado = f"(x - {i})(x + {j})"
                        encontrado = True
                        break
            
            if not encontrado:
                error = "El trinomio no se puede factorizar con números enteros por este método."

        except (ValueError, TypeError):
            error = "Por favor, introduce coeficientes enteros válidos."

    contexto = {
        'resultado': resultado,
        'error': error,
        'v': valores_originales
    }
    return render(request, 'factorizacion/factorizacion.html', contexto)