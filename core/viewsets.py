from rest_framework import viewsets
from core.serializer import PacienteSerializer, ConsultaSerializer
from core.models import Paciente, Consulta

class PacienteViewSets(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()

class ConsultaViewSets(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()