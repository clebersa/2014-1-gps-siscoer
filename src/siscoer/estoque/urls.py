#coding:utf-8
from django.conf.urls import *
from views import *


urlpatterns = patterns('',
    url(r'^start/', 'estoque.views.start', name=start),
    ### Afiliado
    url(r'^home/(?P<username>[\w_-]+)/$', 'estoque.views.home', name=home),
    url(r'^perfil/(?P<username>[\w_-]+)/$', 'estoque.views.perfil', name=perfil),

    url(r'^estoque/(?P<username>[\w_-]+)/$', 'estoque.views.estoque', name=estoque),
    url(r'^cadastrar_estoque/(?P<username>[\w_-]+)/$', 'estoque.views.cadastrar_estoque', name=cadastrar_estoque),
    url(r'^deletar_estoque/(?P<id>[\w_-]+)/(?P<op>[\w_-]+)/$', 'estoque.views.deletar_estoque', name=deletar_estoque),
    url(r'^categoria/(?P<username>[\w_-]+)/$', 'estoque.views.categoria', name=categoria),
    url(r'^cadastrar_categoria/(?P<username>[\w_-]+)/$', 'estoque.views.cadastrar_categoria', name=cadastrar_categoria),
    url(r'^deletar_categoria/(?P<id>[\w_-]+)/(?P<op>[\w_-]+)/$', 'estoque.views.deletar_categoria', name=deletar_categoria),
    url(r'^produto/(?P<username>[\w_-]+)/$', 'estoque.views.produto', name=produto),
    url(r'^cadastrar_produto/(?P<username>[\w_-]+)/$', 'estoque.views.cadastrar_produto', name=cadastrar_produto),
    url(r'^deletar_produto/(?P<id>[\w_-]+)/(?P<op>[\w_-]+)/$', 'estoque.views.deletar_produto', name=deletar_produto),

    url(r'^entrada/(?P<username>[\w_-]+)/$', 'estoque.views.entrada', name=entrada),
    url(r'^cadastrar_entrada/(?P<username>[\w_-]+)/$', 'estoque.views.cadastrar_entrada', name=cadastrar_entrada),
    url(r'^baixa/(?P<username>[\w_-]+)/$', 'estoque.views.baixa', name=baixa),
    url(r'^cadastrar_baixa/(?P<username>[\w_-]+)/$', 'estoque.views.cadastrar_baixa', name=cadastrar_baixa),

    url(r'^ordem_alfabetica/(?P<username>[\w_-]+)/$', 'estoque.views.ordem_alfabetica', name=ordem_alfabetica),
    url(r'^maior_qtd/(?P<username>[\w_-]+)/$', 'estoque.views.maior_qtd', name=maior_qtd),
    url(r'^menor_qtd/(?P<username>[\w_-]+)/$', 'estoque.views.menor_qtd', name=menor_qtd),
    url(r'^proximo_vencer/(?P<username>[\w_-]+)/$', 'estoque.views.proximo_vencer', name=proximo_vencer),
    url(r'^longe_vencer/(?P<username>[\w_-]+)/$', 'estoque.views.longe_vencer', name=longe_vencer),

    url(r'^falta_alfabetica/(?P<username>[\w_-]+)/$', 'estoque.views.falta_alfabetica', name=falta_alfabetica),
    url(r'^data_acabou/(?P<username>[\w_-]+)/$', 'estoque.views.data_acabou', name=data_acabou),

    url(r'^historico_por_estoque/(?P<username>[\w_-]+)/$', 'estoque.views.historico_por_estoque', name=historico_por_estoque),
    url(r'^historico_por_estoque_semanal/(?P<username>[\w_-]+)/$', 'estoque.views.historico_por_estoque_semanal', name=historico_por_estoque_semanal),
    url(r'^historico_por_estoque_quinzenal/(?P<username>[\w_-]+)/$', 'estoque.views.historico_por_estoque_quinzenal', name=historico_por_estoque_quinzenal),
    url(r'^historico_por_estoque_mensal/(?P<username>[\w_-]+)/$', 'estoque.views.historico_por_estoque_mensal', name=historico_por_estoque_mensal),
    url(r'^historico_por_estoque_semestral/(?P<username>[\w_-]+)/$', 'estoque.views.historico_por_estoque_semestral', name=historico_por_estoque_semestral),
    url(r'^historico_por_estoque_anual/(?P<username>[\w_-]+)/$', 'estoque.views.historico_por_estoque_anual', name=historico_por_estoque_anual),
    url(r'^historico_por_produto/(?P<username>[\w_-]+)/$', 'estoque.views.historico_por_produto', name=historico_por_produto),
)
