#coding:utf-8
from django.contrib.admin import site, ModelAdmin

from models import Localizacao, Categoria, Produto, Entrada, Saida


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
    readonly_fields = ['cadastro', 'alteracao',]
    list_display = ['id', 'localizacao', 'categoria', 'descricao', 'unidade', 'cadastro', 'alteracao', ]
    list_display_links = ['id', 'localizacao', 'categoria', 'descricao', 'unidade', 'cadastro', 'alteracao', ]
    search_fields = ['descricao', ]
    list_filter = ['cadastro', 'alteracao',]
    raw_id_fields = ['localizacao', 'categoria',]
    list_per_page = 50


class EntradaAdmin(ModelAdmin):
    model = Entrada
    readonly_fields = ['cadastro', 'alteracao',]
    list_display = ['id', 'produto', 'quantidade', 'valor', 'data_compra', 'cadastro', 'alteracao', ]
    list_display_links = ['id', 'produto', 'quantidade', 'valor', 'cadastro', 'alteracao', ]
    search_fields = ['local_compra', 'produto',]
    list_filter = ['data_compra', 'cadastro', 'alteracao',]
    raw_id_fields = ['produto', ]
    list_per_page = 50


class SaidaAdmin(ModelAdmin):
    model = Saida
    readonly_fields = ['cadastro', 'alteracao',]
    list_display = ['id', 'produto', 'quantidade', 'motivo', 'cadastro', 'alteracao', ]
    list_display_links = ['id', 'produto', 'quantidade', 'motivo', 'cadastro', 'alteracao', ]
    search_fields = ['produto', ]
    list_filter = ['cadastro', 'alteracao',]
    raw_id_fields = ['produto', ]
    list_per_page = 50


site.register(Localizacao, LocalizacaoAdmin)
site.register(Categoria, CategoriaAdmin)
site.register(Produto, ProdutoAdmin)
#site.register(Entrada, EntradaAdmin)
#site.register(Saida, SaidaAdmin)