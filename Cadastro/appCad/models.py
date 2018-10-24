from django.db import models
from django.utils.formats import date_format

# Create your models here.
class Aluno(models.Model):

    nome = models.CharField("Nome", max_length=100)
    cpf = models.CharField("CPF", max_length=14)
    data_nasc = models.DateField("Data de Nascimento")
    endereco = models.CharField("Endereço", max_length=150)
    telefone = models.CharField("Telefone", max_length=11)
    curso = models.CharField("Curso", max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name = (u'nome')
        verbose_name_plural = (u'nomes')


    def __str__(self):
        return self.nome