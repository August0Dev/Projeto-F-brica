from django.db.models import CharField, DecimalField, Model, DateTimeField
from django.utils import timezone

class Paciente(Model):
    nome = CharField(max_length=100)
    idade = CharField(max_length=100)
    sexo = CharField(max_length=100)
    telefone = CharField(max_length=11)
    endereco = CharField(max_length=100)
    horaDeChegada = DateTimeField(default=timezone.now)

class Consulta(Model):
    especialidade = CharField(max_length=100)
    medico = CharField(max_length=100)
    valor = DecimalField(max_digits= 5, decimal_places=2)