from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from pacientes.models import Paciente

# Create your views here.
def pacientes(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()
        queixas = Paciente.queixa_choices
        return render(request, 'pacientes.html', {'queixas': queixas, 'pacientes': pacientes})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0 or not foto:
            messages.add_message(request, constants.ERROR, 'Nome e foto são obrigatórios.')
            return redirect('pacientes')
        
        paciente = Paciente(nome=nome, email=email, telefone=telefone, queixa=queixa, foto=foto)
        paciente.save()
        messages.add_message(request, constants.SUCCESS, 'Paciente cadastrado com sucesso.')
        return redirect('pacientes')
    
def paciente_view(request, id):
    paciente = Paciente.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'paciente.html', {'paciente': paciente})
    
def atualizar_paciente(request, id):
    pagamento_em_dia = request.POST.get('pagamento_em_dia')
    paciente = Paciente.objects.get(id=id)
    status = True if pagamento_em_dia == 'ativo' else False
    paciente.pagamento_em_dia = status
    paciente.save()
    
    return redirect(f'/pacientes/{id}/')