#coding:utf-8
from django.contrib.admin import site, ModelAdmin

from models import Localizacao, Categoria, Produto, Entrada, Baixa


class LocalizacaoAdmin(ModelAdmin):
    model = Localizacao
    readonly_fields = ['cadastro', 'alteracao',]
    list_display = ['id', 'descricao', 'cadastro', 'alteracao', 'ativo',]
    list_display_links = ['id', 'descricao', 'cadastro', 'alteracao', 'ativo',]
    search_fields = ['descricao', ]
    list_filter = ['cadastro', 'alteracao',]
    list_per_page = 50


class CategoriaAdmin(ModelAdmin):
    model = Categoria
    readonly_fields = ['cadastro', 'alteracao',]
    list_display = ['id', 'descricao', 'cadastro', 'alteracao', 'ativo',]
    list_display_links = ['id', 'descricao', 'cadastro', 'alteracao', 'ativo',]
    search_fields = ['descricao', ]
    list_filter = ['cadastro', 'alteracao',]
    list_per_page = 50


class ProdutoAdmin(ModelAdmin):
    model = Produto
    readonly_fields = ['cadastro', 'alteracao', 'quantidade',]
    list_display = ['id', 'categoria', 'descricao', 'unidade', 'quantidade', 'cadastro', 'alteracao', ]
    list_display_links = ['id', 'categoria', 'descricao', 'unidade', 'quantidade', 'cadastro', 'alteracao', ]
    search_fields = ['descricao', ]
    list_filter = ['cadastro', 'alteracao',]
    raw_id_fields = ['categoria',]
    list_per_page = 50


class EntradaAdmin(ModelAdmin):
    model = Entrada
    readonly_fields = ['cadastro', 'alteracao',]
    list_display = ['id', 'localizacao', 'produto', 'quantidade', 'valor', 'data_compra', 'cadastro', 'alteracao', 'finalizado',]
    list_display_links = ['id', 'localizacao', 'produto', 'quantidade', 'valor', 'cadastro', 'alteracao', 'finalizado',]
    search_fields = ['local_compra', 'produto',]
    list_filter = ['data_compra', 'cadastro', 'alteracao',]
    raw_id_fields = ['produto', 'localizacao',]
    list_per_page = 50


class BaixaAdmin(ModelAdmin):
    model = Baixa
    readonly_fields = ['cadastro', 'alteracao',]
    list_display = ['id', 'entrada', 'quantidade', 'motivo', 'cadastro', 'alteracao', ]
    list_display_links = ['id', 'entrada', 'quantidade', 'motivo', 'cadastro', 'alteracao', ]
    search_fields = ['entrada', ]
    list_filter = ['cadastro', 'alteracao',]
    raw_id_fields = ['entrada', ]
    list_per_page = 50


site.register(Localizacao, LocalizacaoAdmin)
site.register(Categoria, CategoriaAdmin)
site.register(Produto, ProdutoAdmin)
site.register(Entrada, EntradaAdmin)
site.register(Baixa, BaixaAdmin)