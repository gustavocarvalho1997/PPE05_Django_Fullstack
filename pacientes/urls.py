from django.urls import path
from pacientes.views import pacientes, paciente_view, atualizar_paciente, excluir_consulta, consulta_publica

urlpatterns = [
    path('', pacientes, name='pacientes'),
    path('<int:id>/', paciente_view, name='paciente_view'),
    path('atualizar_paciente/<int:id>/', atualizar_paciente, name='atualizar_paciente'),
    path('excluir_consulta/<int:id>/', excluir_consulta, name='excluir_consulta'),
    path('consulta_publica/<int:id>/', consulta_publica, name='consulta_publica')
]