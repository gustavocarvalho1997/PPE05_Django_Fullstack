from django.urls import path
from pacientes.views import pacientes, paciente_view

urlpatterns = [
    path('', pacientes, name='pacientes'),
    path('<int:id>/', paciente_view, name='paciente_view'),
]