from django.db import models

# Create your models here.

class Participante(models.Model):
    SEXO_CHOICE = [
        ('M', "Masculino"),
        ('F', "Feminino")
    ]

    ESCOLARIDADE_CHOICE = [
        ('FC', "Fundamental Completo"),
        ('FI', "Fundamental Incompleto"),
        ('MC', "Médio Completo"),
        ('MI', "Médio Incompleto"),
        ('SC', "Superior Completo"),
        ('SI', "Superior Incompleto"),
        ('PG', "Pós Graduação"),
        ('SF', "Sem Formação"),
    ]
    
    Nome = models.CharField(max_length=100,blank=True,verbose_name="Nome Completo")
    cpf = models.CharField(max_length=11, verbose_name="CPF", blank=True)
    sexo = models.CharField(max_length=1,choices=SEXO_CHOICE)
    nascimento = models.DateField(blank=True)
    Endereço = models.CharField(max_length=50)
    Celular = models.CharField(max_length=13, blank=True)
    Email = models.EmailField()
    Cep = models.CharField(max_length=8,verbose_name="CEP")
    Cidade = models.CharField(max_length=30)
    Escolaridade = models.CharField(choices=ESCOLARIDADE_CHOICE, max_length=2)
    termo = models.FileField(blank=True, verbose_name="termo de compromisso", upload_to="", default= " ")
    
    def __str__(self):
        return str(self.id)

class Empresa(models.Model):

    EMPRESA_CHOICE = [
        ('EMC', "Empresa Com CNPJ"),
        ('PRD', "Produtor Rural DAP")
    ]

    SETOR_CHOICE = [
        ('A', "Agronegócio"),
        ('C', "Comércio"),
        ('I', "Indústria"),
        ('S', "Serviço")
    ]


    cnpj_dap = models.CharField(blank=True,max_length=14, verbose_name="CNPJ OU DAP")
    Setor = models.CharField(choices=SETOR_CHOICE, max_length=1)
    razao = models.CharField(blank=True, verbose_name="Razão Social", max_length=40)
    endereço = models.CharField(max_length=50)
    celular = models.CharField(max_length=13, blank=True)
    email = models.EmailField()
    data_abertura = models.DateField(verbose_name="Data de Abertura")
    tipo_empresa = models.CharField(verbose_name="Tipo de Empresa", choices=EMPRESA_CHOICE, max_length=3)



    

    



