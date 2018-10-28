#Vamos criar as views, abra o arquivo views.py
# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from appCad.models import Aluno
from appCad.forms import FormAluno
from django.http import HttpResponse
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

def home(request):
        return render(request,'index.html')

class Criar(CreateView):
        form_class = FormAluno
        template_name = 'cadastro.html'
        model = Aluno
        success_url = reverse_lazy('lista')

class Lista(ListView):
        template_name = 'lista.html'
        model = Aluno
        context_object = 'nome'
        fields = "__all__"

class DeletaAluno(DeleteView):
        form_class = FormAluno
        model = Aluno
        success_url = reverse_lazy('lista')


class AlteraAluno(UpdateView):
        template_name = 'cadastro.html'
        model = Aluno
        fields = "__all__" 
        success_url = reverse_lazy('lista')