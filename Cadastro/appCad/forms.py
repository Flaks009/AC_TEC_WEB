#Criando o arquivo forms.py

from django import forms
from .import models

class FormAluno(forms.ModelForm):

      class Meta:
            model = models.Aluno
            fields = ['nome','cpf','data_nasc','endereco','telefone', 'curso']