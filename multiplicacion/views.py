from django.shortcuts import render

# Create your views here.

def multiplicacion_view(request):
    resultado = None
    error = None
    valores_originales = {}

    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            resultado = num1 * num2
            valores_originales = {'num1': num1, 'num2': num2}
        except (ValueError, TypeError):
            error = "Por favor, introduce números válidos."

    contexto = {
        'resultado': resultado,
        'error': error,
        'valores': valores_originales
    }
    return render(request, 'multiplicacion/multiplicacion.html', contexto)