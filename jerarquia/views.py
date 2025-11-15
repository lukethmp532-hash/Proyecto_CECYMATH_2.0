# jerarquia/views.py

from django.shortcuts import render

def jerarquia_view(request):
    resultado = None
    error = None
    expresion_original = ""
    
    # Si el método es POST, se realizan los cálculos
    if request.method == 'POST':
        expresion = request.POST.get('expresion', '')
        expresion_original = expresion
        try:
            # --- ¡ADVERTENCIA DE SEGURIDAD! ---
            resultado = eval(expresion)
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            # Esta es la línea que cambiamos para compatibilidad con el linter
            error = "Error en la expresión: '" + str(e) + "'"
        except Exception as e:
            error = "Ocurrió un error inesperado al evaluar la expresión."
    # --- ESTAS LÍNEAS AHORA ESTÁN FUERA DEL 'IF' ---
    # Se ejecutan siempre, tanto en GET como en POST.
    
    # Preparamos el contexto con las variables para el HTML
    contexto = {
        'resultado': resultado,
        'error': error,
        'expresion_original': expresion_original,
    }
    
    # Renderizamos la página HTML y le pasamos el contexto
    return render(request, 'jerarquia/jerarquia.html', contexto)