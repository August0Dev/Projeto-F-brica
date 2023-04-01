from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clinica_medica.api.viewsets import PacienteViewSets, ConsultaViewSets


route = routers.DefaultRouter()

route.register('Paciente/', PacienteViewSets, basename = "Pacientes")
route.register('Consulta/', ConsultaViewSets, basename = "Consultas")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
