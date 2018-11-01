#Vamos criar as views, abra o arquivo views.py
# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from appCad.models import Aluno, Professor, Disciplina
from appCad.forms import FormAluno, FormProf, FormDis
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

class CriarProf(CreateView):
        form_class = FormProf
        template_name = 'cadastro-prof.html'
        model = Professor
        success_url = reverse_lazy('lista-prof')

class CriarDis(CreateView):
        form_class = FormDis
        template_name = 'cadastro-disciplina.html'
        model = Disciplina
        success_url = reverse_lazy('lista-disciplina')

class Lista(ListView):
        template_name = 'lista.html'
        model = Aluno
        context_object = 'nome'
        fields = "__all__"

class ListaProf(ListView):
        template_name = 'lista-prof.html'
        model = Professor
        context_object = 'nome'
        fields = "__all__"

class ListaDis(ListView):
        template_name = 'lista-disciplina.html'
        model = Disciplina
        context_object = 'nome'
        fields = "__all__"

class DeletaAluno(DeleteView):
        form_class = FormAluno
        model = Aluno
        success_url = reverse_lazy('lista')

class DeletaProf(DeleteView):
        form_class = FormProf
        model = Professor
        success_url = reverse_lazy('lista-prof')

class DeletaDis(DeleteView):
        form_class = FormDis
        model = Disciplina
        success_url = reverse_lazy('lista-disciplina')


class AlteraAluno(UpdateView):
        template_name = 'cadastro.html'
        model = Aluno
        fields = "__all__" 
        success_url = reverse_lazy('lista')

class AlteraProf(UpdateView):
        template_name = 'cadastro-prof.html'
        model = Professor
        fields = "__all__" 
        success_url = reverse_lazy('lista-prof')

class AlteraDis(UpdateView):
        template_name = 'cadastro-disciplina.html'
        model = Disciplina
        fields = "__all__" 
        success_url = reverse_lazy('lista-disciplina')