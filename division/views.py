# division/views.py

from django.shortcuts import render

def division_view(request):
    resultado = None
    error = None
    if request.method == 'POST':
        try:
            dividendo = float(request.POST.get('dividendo'))
            divisor = float(request.POST.get('divisor'))

            if divisor == 0:
                error = "Error: No se puede dividir por cero."
            else:
                resultado = dividendo / divisor
        except (ValueError, TypeError):
            error = "Por favor, introduce números válidos."

    return render(request, 'division/division.html', {'resultado': resultado, 'error': error})