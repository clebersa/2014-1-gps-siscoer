#coding:utf-8
from django.core.urlresolvers import reverse
from django.db.models import Model, CharField, ForeignKey, EmailField, DateTimeField, BooleanField, DateField, \
    PositiveIntegerField, PositiveSmallIntegerField, DecimalField
from django.utils.translation import ugettext_lazy as _


class Localizacao(Model):
    class Meta:
        verbose_name = _(u'Local. Estoque')
        verbose_name_plural = _(u'1 - Local. Estoque')
    descricao = CharField(verbose_name=_(u'Identificação'), max_length=100, help_text=_(u'Local. Estoque. Ex.: Casa da Praia, Apartamento, Empresa, etc.'))
    cadastro = DateTimeField(verbose_name=_(u'Data de Cadastro'), auto_now_add=True, editable=False)
    alteracao = DateTimeField(verbose_name=_(u'Data de Alteração'), auto_now=True, editable=False)
    ativo = BooleanField(verbose_name=_(u'Ativo?'), default=True, editable=False)

    def __unicode__(self):
        return u'%s' % self.descricao


class Categoria(Model):
    class Meta:
        verbose_name = _(u'Categoria')
        verbose_name_plural = _(u'2 - Categoria')
    descricao = CharField(verbose_name=_(u'Categoria'), max_length=100, help_text=_(u'Nome da Categoria. Ex.: Alimentos, Higiene, etc.'))
    cadastro = DateTimeField(verbose_name=_(u'Data de Cadastro'), auto_now_add=True, editable=False)
    alteracao = DateTimeField(verbose_name=_(u'Data de Alteração'), auto_now=True, editable=False)
    ativo = BooleanField(verbose_name=_(u'Ativa?'), default=True, editable=False)

    def __unicode__(self):
        return u'%s' % self.descricao


class Produto(Model):
    UNIDADE = (
        (0,_(u'Unidade')),
        (1,_(u'Litro(s)')),
        (2,_(u'Metro(s)')),
        (3,_(u'Quilograma(s)')),
        #(4,_(u'Caixa(s)')),
    )
    class Meta:
        verbose_name = _(u'Produto')
        verbose_name_plural = _(u'3 - Produto')
    localizacao = ForeignKey('Localizacao', verbose_name=_(u'Estoque'),)
    categoria = ForeignKey('Categoria', verbose_name=_(u'Categoria'),)
    descricao = CharField(verbose_name=_(u'Categoria'), max_length=150, help_text=_(u'Nome da Categoria. Ex.: Alimentos, Higiene, etc.'))
    unidade = PositiveSmallIntegerField(verbose_name=_(u'Unidade'), choices=UNIDADE, default=None)
    quantidade = PositiveIntegerField(verbose_name=_(u'Quantidade'), blank=True, null=True, default=0)
    validade = DateField(verbose_name=_(u'Data Validade'), blank=True, null=True, )
    valor_ultima_compra = DecimalField(verbose_name=_(u'Valor Última Compra'), decimal_places=2, max_digits=9, blank=True, null=True, )
    local_Ultima_compra = CharField(verbose_name=_(u'Local Última Compra'), max_length=100, help_text=_(u'Ex.: Sup. Imperador, Bretas, etc.'), blank=True, null=True, )
    data_ultima_compra = DateField(verbose_name=_(u'Data Última Compra'), blank=True, null=True, )
    cadastro = DateTimeField(verbose_name=_(u'Data Cadastro'), auto_now_add=True, editable=False)
    alteracao = DateTimeField(verbose_name=_(u'Data Alteração'), auto_now=True, editable=False)

    def __unicode__(self):
        return u'%s' % self.descricao


class Entrada(Model):
    class Meta:
        verbose_name = _(u'Entrada')
        verbose_name_plural = _(u'4 - Entrada')
    produto = ForeignKey('Produto', verbose_name=_(u'Produto'),)
    quantidade = PositiveIntegerField(verbose_name=_(u'Quantidade'), blank=True, null=True, default=0)
    validade = DateField(verbose_name=_(u'Data Validade'), blank=True, null=True, )
    valor = DecimalField(verbose_name=_(u'Preço'), decimal_places=2, max_digits=9, blank=True, null=True, )
    local_compra = CharField(verbose_name=_(u'Local Compra'), max_length=100, help_text=_(u'Ex.: Sup. Imperador, Bretas, etc.'), blank=True, null=True, )
    data_compra = DateField(verbose_name=_(u'Data Compra'), blank=True, null=True, )
    cadastro = DateTimeField(verbose_name=_(u'Data Cadastro'), auto_now_add=True, editable=False)
    alteracao = DateTimeField(verbose_name=_(u'Data Alteração'), auto_now=True, editable=False)

    def __unicode__(self):
        return u'%s - %s' % (self.id, self.produto.descricao)


class Saida(Model):
    class Meta:
        verbose_name = _(u'Saída')
        verbose_name_plural = _(u'5 - Saída')
    produto = ForeignKey('Produto', verbose_name=_(u'Produto'),)
    quantidade = PositiveIntegerField(verbose_name=_(u'Quantidade'), blank=True, null=True, default=0)
    motivo = CharField(verbose_name=_(u'Motivo'), max_length=100, help_text=_(u'Ex.: Consumiu, Estragou, Doação e Outro.'), blank=True, null=True, )
    cadastro = DateTimeField(verbose_name=_(u'Data Cadastro'), auto_now_add=True, editable=False)
    alteracao = DateTimeField(verbose_name=_(u'Data Alteração'), auto_now=True, editable=False)

    def __unicode__(self):
        return u'%s - %s' % (self.id, self.produto.descricao)