from django.shortcuts import render

# Create your views here.
def pacientes(request):
    return render(request, 'pacientes.html')