# polinomios/views.py

from django.shortcuts import render

def polinomios_view(request):
    resultado = None
    error = None
    polinomios_originales = {}

    if request.method == 'POST':
        try:
            # Coeficientes del primer polinomio (ax^2 + bx + c)
            a1 = float(request.POST.get('a1', 0))
            b1 = float(request.POST.get('b1', 0))
            c1 = float(request.POST.get('c1', 0))
            
            # Coeficientes del segundo polinomio (dx^2 + ex + f)
            a2 = float(request.POST.get('a2', 0))
            b2 = float(request.POST.get('b2', 0))
            c2 = float(request.POST.get('c2', 0))

            polinomios_originales = {'a1': a1, 'b1': b1, 'c1': c1, 'a2': a2, 'b2': b2, 'c2': c2}

            # Sumamos los coeficientes correspondientes
            sum_a = a1 + a2
            sum_b = b1 + b2
            sum_c = c1 + c2

            # Formateamos el resultado para mostrarlo de forma legible
            resultado = f"{sum_a}x² + {sum_b}x + {sum_c}".replace('+ -', '- ')

        except (ValueError, TypeError):
            error = "Por favor, introduce coeficientes numéricos válidos."

    contexto = {
        'resultado': resultado,
        'error': error,
        'p': polinomios_originales # Abreviatura para el diccionario
    }
    return render(request, 'polinomios/polinomios.html', contexto)