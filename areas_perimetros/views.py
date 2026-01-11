# areas_perimetros/views.py

from django.shortcuts import render
import math

def areas_perimetros_view(request):
    resultado = None
    error = None

    if request.method == 'POST':
        figura = request.POST.get('figura', '')
        try:
            if figura == 'cuadrado':
                lado = float(request.POST.get('lado'))
                area = lado ** 2
                perimetro = 4 * lado
                resultado = f"Cuadrado: Área = {area:.2f}, Perímetro = {perimetro:.2f}"
            
            elif figura == 'rectangulo':
                base = float(request.POST.get('base'))
                altura = float(request.POST.get('altura'))
                area = base * altura
                perimetro = 2 * (base + altura)
                resultado = f"Rectángulo: Área = {area:.2f}, Perímetro = {perimetro:.2f}"

            elif figura == 'circulo':
                radio = float(request.POST.get('radio'))
                area = math.pi * (radio ** 2)
                perimetro = 2 * math.pi * radio
                resultado = f"Círculo: Área = {area:.2f}, Perímetro (Circunferencia) = {perimetro:.2f}"

            elif figura == 'triangulo':
                base_t = float(request.POST.get('base_t'))
                altura_t = float(request.POST.get('altura_t'))
                area = (base_t * altura_t)/2
                # Asumimos un triángulo rectángulo para un cálculo de perímetro simple
                perimetro = base_t  * 3
                resultado = f"Triángulo Equilatero: Área = {area:.2f}, Perímetro = {perimetro:.2f}"

        except (ValueError, TypeError):
            error = "Por favor, introduce valores numéricos válidos para la figura seleccionada."

    contexto = {'resultado': resultado, 'error': error}
    return render(request, 'areas_perimetros/areas_perimetros.html', contexto)