from django.shortcuts import render

def suma_view(request):
    resultado = None
    error = None
    valores_originales = {}

    if request.method == 'POST':
        try:
            numero1 = float(request.POST.get('numero1'))
            numero2 = float(request.POST.get('numero2'))
            valores_originales = {'numero1': numero1, 'numero2': numero2}
            resultado = numero1 + numero2
        except (ValueError, TypeError):
            error = "Por favor, introduce números válidos."

    contexto = {
        'resultado': resultado,
        'error': error,
        'valores_originales': valores_originales
    }
    return render(request, 'suma/suma.html', contexto)