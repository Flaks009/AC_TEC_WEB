#Definindo a url do projeto. Abra o arquivo urls.py
from appCad import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

app_name = 'appCad'

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^cadastro/$', views.Criar.as_view(), name='cadastro'),
    url(r'^cadastro-prof/$', views.CriarProf.as_view(), name='cadastro-prof'),
    url(r'^cadastro-dis/$', views.CriarDis.as_view(), name='cadastro-disciplina'),
    url(r'^lista/$', views.Lista.as_view(), name='lista'),
    url(r'^lista-prof/$', views.ListaProf.as_view(), name='lista-prof'),
    url(r'^lista-dis/$', views.ListaDis.as_view(), name='lista-disciplina'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.DeletaAluno.as_view(), name='deleta'),
    url(r'^delete-prof/(?P<pk>[0-9]+)$', views.DeletaProf.as_view(), name='deleta-prof'),
    url(r'^delete-dis/(?P<pk>[0-9]+)$', views.DeletaDis.as_view(), name='deleta-disciplina'),
    url(r'^cadastro/(?P<pk>[0-9]+)$', views.AlteraAluno.as_view(), name='altera'),
    url(r'^cadastro-prof/(?P<pk>[0-9]+)$', views.AlteraProf.as_view(), name='altera-prof'),
    url(r'^cadastro-dis/(?P<pk>[0-9]+)$', views.AlteraDis.as_view(), name='altera-disciplina'),

    #url(r'^admin/', include(admin.site.urls)),
]   