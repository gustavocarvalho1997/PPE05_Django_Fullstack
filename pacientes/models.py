from django.db import models

# Create your models here.
class Paciente(models.Model):
    queixa_choices = (
        ('TDAH', 'TDAH'),
        ('D', 'Depressão'),
        ('A', 'Ansiedade'),
        ('O', 'Obsessão'),
        ('P', 'Pânico'),
        ('TAG', 'Transtorno de Ansiedade Generalizada'),
    )

    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=255, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos')
    pagamento_em_dia = models.BooleanField(default=True)
    queixa = models.CharField(max_length=4, choices=queixa_choices)

    def __str__(self):
        return self.nome