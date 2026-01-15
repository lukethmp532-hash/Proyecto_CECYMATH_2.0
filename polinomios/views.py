from django.shortcuts import render
from sympy import symbols, expand, latex


from sympy.parsing.sympy_parser import (
    parse_expr, 
    standard_transformations, 
    implicit_multiplication_application, 
    convert_xor
)

def polinomios_view(request):
    resultado = None
    error = None
    valores_originales = {
        'p1': '',
        'p2': '',
        'op': 'suma'
    }

    if request.method == 'POST':
        p1_raw = request.POST.get('polinomio1', '')
        p2_raw = request.POST.get('polinomio2', '')
        operacion = request.POST.get('operacion', 'suma')

        valores_originales = {
            'p1': p1_raw,
            'p2': p2_raw,
            'op': operacion
        }

        try:
            # Definimos las transformaciones:
            # 1. standard_transformations: Reglas básicas de Python.
            # 2. implicit_multiplication_application: Permite escribir "2x" en vez de "2*x".
            # 3. convert_xor: Convierte el símbolo "^" en potencia "**".
            transformaciones = (standard_transformations + (implicit_multiplication_application, convert_xor))

            # Usamos parse_expr con las transformaciones en lugar de sympify directo
            poly1 = parse_expr(p1_raw, transformations=transformaciones)
            poly2 = parse_expr(p2_raw, transformations=transformaciones)

            # Realizar la operación seleccionada
            res_sympy = None
            
            if operacion == 'suma':
                res_sympy = poly1 + poly2
            elif operacion == 'resta':
                res_sympy = poly1 - poly2
            elif operacion == 'multiplicacion':
                res_sympy = expand(poly1 * poly2)
            else:
                error = "Operación no válida."

            # Formatear a LaTeX para que se vea bonito en el HTML
            if res_sympy is not None:
                resultado = latex(res_sympy)

        except Exception as e:
            # Mensaje de error amigable
            error = f"No pudimos entender el polinomio. Asegúrate de usar 'x' u otras letras y números. (Error técnico: {e})"

    contexto = {
        'resultado': resultado,
        'error': error,
        'v': valores_originales
    }

    return render(request, 'polinomios/polinomios.html', contexto)