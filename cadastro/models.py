from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)

    class Meta:
        abstract = True

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=18, unique=True)
    razao_social = models.CharField(max_length=200)