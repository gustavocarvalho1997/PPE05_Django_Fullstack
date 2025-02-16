from django.urls import path
from pacientes.views import pacientes, paciente_view, atualizar_paciente

urlpatterns = [
    path('', pacientes, name='pacientes'),
    path('<int:id>/', paciente_view, name='paciente_view'),
    path('atualizar_paciente/<int:id>/', atualizar_paciente, name='atualizar_paciente'),
]