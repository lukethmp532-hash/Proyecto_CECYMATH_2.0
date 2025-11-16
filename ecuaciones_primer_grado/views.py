# ecuaciones_primer_grado/views.py

from django.shortcuts import render

def primer_grado_view(request):
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
                error = "El coeficiente 'a' no puede ser cero en una ecuación de primer grado."
            else:
                # Despejamos x: ax = c - b  =>  x = (c - b) / a
                x = (c - b) / a
                resultado = f"El valor de x es: {x}"

        except (ValueError, TypeError):
            error = "Por favor, introduce coeficientes numéricos válidos."

    contexto = {
        'resultado': resultado,
        'error': error,
        'v': valores_originales
    }
    return render(request, 'ecuaciones_primer_grado/primer_grado.html', contexto)