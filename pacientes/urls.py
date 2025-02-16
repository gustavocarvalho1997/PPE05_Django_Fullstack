from django.urls import path
from pacientes.views import pacientes

urlpatterns = [
    path('', pacientes, name='pacientes'),
]