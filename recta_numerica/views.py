# recta_numerica/views.py

from django.shortcuts import render

def recta_numerica_view(request):
    puntos = None
    error = None
    numeros_originales = ""

    if request.method == 'POST':
        numeros_str = request.POST.get('numeros', '')
        numeros_originales = numeros_str
        
        if not numeros_str:
            error = "Por favor, introduce al menos un número."
        else:
            try:
                # 1. Convertimos el texto de entrada en una lista de números únicos
                numeros = sorted(list(set(float(num.strip()) for num in numeros_str.split(','))))

                # 2. Encontramos el rango de la recta (mínimo y máximo)
                min_val = min(numeros)
                max_val = max(numeros)
                rango = max_val - min_val

                puntos = []
                # 3. Calculamos la posición de cada punto en la recta
                for num in numeros:
                    posicion_porcentual = 0
                    # Evitamos la división por cero si solo hay un número
                    if rango > 0:
                        posicion_porcentual = ((num - min_val) / rango) * 100
                    else:
                        posicion_porcentual = 50 # Si solo hay un punto, lo centramos

                    puntos.append({
                        'valor': num,
                        'posicion': posicion_porcentual
                    })

            except ValueError:
                error = "Error: Asegúrate de introducir solo números separados por comas."
            except Exception as e:
                error = f"Ocurrió un error inesperado: {e}"

    contexto = {
        'puntos': puntos,
        'error': error,
        'numeros_originales': numeros_originales
    }
    return render(request, 'recta_numerica/recta_numerica.html', contexto)