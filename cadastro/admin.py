from django.contrib import admin
from .models import PessoaFisica, PessoaJuridica

# Register your models here.
@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = 'nome', 'email', 'cpf','data_nascimento',

@admin.register(PessoaJuridica)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    list_display = 'nome', 'email', 'cnpj','razao_social',