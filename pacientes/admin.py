from django.contrib import admin
from pacientes.models import Paciente, Tarefas

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Tarefas)