from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from pacientes.models import Paciente, Tarefa, Consulta

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
        tarefas = Tarefa.objects.all()
        consultas = Consulta.objects.filter(paciente=paciente)
        return render(request, 'paciente.html', {'paciente': paciente, 'tarefas': tarefas, 'consultas': consultas})
    elif request.method == 'POST':
        humor = request.POST.get('humor')
        registro_geral = request.POST.get('registro_geral')
        video = request.FILES.get('video')
        tarefas = request.POST.getlist('tarefas')

        consulta = Consulta(
            humor=int(humor),
            registro_geral=registro_geral,
            video=video,
            paciente=paciente
        )
        consulta.save()

        for tarefa in tarefas:
            consulta.tarefas.add(tarefa)

        consulta.save()
        messages.add_message(request, constants.SUCCESS, 'Registro de consulta cadastrada com sucesso.')
        return redirect(f'/pacientes/{id}/')
    
def atualizar_paciente(request, id):
    pagamento_em_dia = request.POST.get('pagamento_em_dia')
    paciente = Paciente.objects.get(id=id)
    status = True if pagamento_em_dia == 'ativo' else False
    paciente.pagamento_em_dia = status
    paciente.save()
    
    return redirect(f'/pacientes/{id}/')

def excluir_consulta(request, id):
    consulta = Consulta.objects.get(id=id)
    paciente_id = consulta.paciente.id
    consulta.delete()
    return redirect(f'/pacientes/{paciente_id}/')