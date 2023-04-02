from django.contrib import admin
from .models import Paciente, Consulta

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo', 'telefone', 'endereco')

admin.site.register(Paciente, PacienteAdmin)

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('especialidade', 'medico', 'valor')

admin.site.register(Consulta, ConsultaAdmin)


