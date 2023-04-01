from django.db import models
from uuid import uuid4


class Paciente(models.Model):
    id_paciente = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    endereco =models.CharField(max_length=100)


class Consulta(models.Model):
    especialidade = models.CharField(max_length=100)
    medico = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=3, decimal_places=2)


