from django.shortcuts import render
# Create your views here.

def agradecimientos(request):
    return render(request, 'agradecimientos/agradecimientos.html')