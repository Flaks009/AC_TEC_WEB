#Criando o arquivo forms.py

from django import forms
from .import models

class FormAluno(forms.ModelForm):

      class Meta:
            model = models.Aluno
            fields = "__all__"