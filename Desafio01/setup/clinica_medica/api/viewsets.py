from rest_framework import viewsets
from clinica_medica.api.serializers import PacienteSerializer, ConsultaSerializer
from clinica_medica.models import Paciente, Consulta

class PacienteViewSets(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()


class ConsultaViewSets(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()