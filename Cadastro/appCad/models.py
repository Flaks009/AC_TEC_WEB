from django.db import models
from django.utils.formats import date_format

# Create your models here.
class Aluno(models.Model):

    nome = models.CharField("Nome", max_length=100)
    cpf = models.CharField("CPF(Somente números)", max_length=11)
    data_nasc = models.DateField("Data de Nascimento (aaaa-mm-dd)")
    endereco = models.CharField("Endereço", max_length=150)
    telefone = models.CharField("Telefone", max_length=11)
    curso = models.CharField("Curso", max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name = (u'nome')
        verbose_name_plural = (u'nomes')


    def __str__(self):
        return self.nome


class Professor(models.Model):

    nome = models.CharField("Nome", max_length=100)
    cpf = models.CharField("CPF(Somente números)", max_length=11)
    data_nasc = models.DateField("Data de Nascimento (aaaa-mm-dd)")
    endereco = models.CharField("Endereço", max_length=150)
    telefone = models.CharField("Telefone", max_length=11)
    materia = models.CharField("Materia ministrada", max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name = (u'nome')
        verbose_name_plural = (u'nomes')


    def __str__(self):
        return self.nome

class Disciplina(models.Model):

    nome = models.CharField("Nome", max_length=100)
    profresp = models.CharField("Professores Responsáveis", max_length=100)
    carga = models.IntegerField("Carga Horária")
    coordenador = models.CharField("Coordenador Responsável", max_length=100)
    conteudo = models.CharField("Conteudo Programático", max_length=500)
    curso = models.CharField("Cursos Ministrados", max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name = (u'nome')
        verbose_name_plural = (u'nomes')


    def __str__(self):
        return self.nome