#coding:utf-8
from django.contrib.admin import site, ModelAdmin

from models import Usuario
from forms import UsuarioForm


class UsuarioAdmin(ModelAdmin):
    model = Usuario
    form = UsuarioForm
    exclude = ['user',]
    readonly_fields = ['cadastro', 'alteracao',]
    list_display = ['id', 'login', 'mail', 'cadastro', 'alteracao',]
    list_display_links = ['id', 'login', 'mail', 'cadastro', 'alteracao',]
    search_fields = ['login', 'mail',]
    list_filter = ['cadastro', 'alteracao',]
    list_per_page = 50


site.register(Usuario, UsuarioAdmin)
