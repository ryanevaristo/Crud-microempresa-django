from django.contrib import admin

# Register your models here.
from core.models import Participante, Empresa
@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['id','Nome','cpf','sexo','Celular']
    search_fields = ['cpf']


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display= ['id','razao','cnpj_dap','tipo_empresa', 'data_abertura' ]
    search_fields = ['cnpj_dap']


