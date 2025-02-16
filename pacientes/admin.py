from django.contrib import admin
from pacientes.models import Paciente, Tarefa

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Tarefa)