#Criando o arquivo forms.py

from django import forms
from .import models
import re

class FormAluno(forms.ModelForm):
            
      def clean(self): 
            # data from the form is fetched using super function 
            super(FormAluno, self).clean()
            nome = self.cleaned_data.get('nome')
            cpf = self.cleaned_data.get('cpf')
            telefone = self.cleaned_data.get('telefone')
            curso = self.cleaned_data.get('curso')
            if nome.isspace() == True:
                  if nome.isalpha() == False:
                        self._errors['nome'] = self.error_class(['Digite apenas letras'])
            if cpf.isdigit() == False:
                  self._errors['cpf'] = self.error_class(['Digite apenas numeros'])
            if len(cpf) != 11:
                  self._errors['cpf'] = self.error_class(['O CPF deve conter 11 digitos'])                  
            if telefone.isdigit() == False:
                  self._errors['telefone'] = self.error_class(['Digite apenas numeros'])
            if len(telefone) > 9 or len(telefone) < 8  == False:
                  self._errors['telefone'] = self.error_class(['O telefone deve conter de 8 a 9 digitos'])
            if curso.isalpha() == False:
                  self._errors['curso'] = self.error_class(['Digite apenas letras'])

            return self.cleaned_data

      class Meta:
            model = models.Aluno
            fields = ['nome','cpf','data_nasc','endereco','telefone', 'curso']