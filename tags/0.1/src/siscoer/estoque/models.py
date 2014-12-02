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

    def get_absolute_url(self):
        return reverse('estoque.views.deletar_estoque', kwargs={'id': self.id, 'op': 0})


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

    def get_absolute_url(self):
        return reverse('estoque.views.deletar_categoria', kwargs={'id': self.id, 'op': 0})


class Produto(Model):
    UNIDADE = (
        (0,_(u'Unidade')),
        (1,_(u'Litro(s)')),
        (2,_(u'Metro(s)')),
        (3,_(u'Quilograma(s)')),
    )
    class Meta:
        verbose_name = _(u'Produto')
        verbose_name_plural = _(u'3 - Produto')
    categoria = ForeignKey('Categoria', verbose_name=_(u'Categoria'),)
    descricao = CharField(verbose_name=_(u'Descrição'), max_length=150, help_text=_(u'Nome da Categoria. Ex.: Alimentos, Higiene, etc.'))
    unidade = PositiveSmallIntegerField(verbose_name=_(u'Unidade'), choices=UNIDADE, default=None)
    quantidade = PositiveIntegerField(verbose_name=_(u'Quantidade'), blank=True, null=True, default=0)
    cadastro = DateTimeField(verbose_name=_(u'Data Cadastro'), auto_now_add=True, editable=False)
    alteracao = DateTimeField(verbose_name=_(u'Data Alteração'), auto_now=True, editable=False)

    def __unicode__(self):
        return u'%s' % self.descricao

    def get_absolute_url(self):
        return reverse('estoque.views.deletar_produto', kwargs={'id': self.id, 'op': 0})


class Entrada(Model):
    class Meta:
        verbose_name = _(u'Entrada')
        verbose_name_plural = _(u'4 - Entrada')
    localizacao = ForeignKey('Localizacao', verbose_name=_(u'Estoque'),)
    produto = ForeignKey('Produto', verbose_name=_(u'Produto'),)
    quantidade = PositiveIntegerField(verbose_name=_(u'Quantidade'), blank=True, null=True, default=0)
    validade = DateField(verbose_name=_(u'Data Validade'), blank=True, null=True, )
    valor = DecimalField(verbose_name=_(u'Preço'), decimal_places=2, max_digits=9, blank=True, null=True, )
    local_compra = CharField(verbose_name=_(u'Local Compra'), max_length=100, help_text=_(u'Ex.: Sup. Imperador, Bretas, etc.'), blank=True, null=True, )
    data_compra = DateField(verbose_name=_(u'Data Compra'), blank=True, null=True, )
    finalizado = BooleanField(verbose_name=_(u'Finalizado?'), default=False, editable=False)
    cadastro = DateTimeField(verbose_name=_(u'Data Cadastro'), auto_now_add=True, editable=False)
    alteracao = DateTimeField(verbose_name=_(u'Data Alteração'), auto_now=True, editable=False)

    def __unicode__(self):
        return u'%s - %s - %s - %s' % (self.localizacao.descricao, self.produto.descricao, self.produto.get_unidade_display(), self.quantidade)


class Baixa(Model):
    MOTIVO = (
        (0,_(u'Consumiu')),
        (1,_(u'Estragou')),
        (2,_(u'Doação')),
        (3,_(u'Outro(s)')),
    )
    class Meta:
        verbose_name = _(u'Baixa')
        verbose_name_plural = _(u'5 - Baixa')
    entrada = ForeignKey('Entrada', verbose_name=_(u'Produto'),)
    quantidade = PositiveIntegerField(verbose_name=_(u'Quantidade'), blank=True, null=True, default=0)
    motivo = PositiveSmallIntegerField(verbose_name=_(u'Motivo'), choices=MOTIVO, default=None)
    cadastro = DateTimeField(verbose_name=_(u'Data Cadastro'), auto_now_add=True, editable=False)
    alteracao = DateTimeField(verbose_name=_(u'Data Alteração'), auto_now=True, editable=False)

    def __unicode__(self):
        return u'%s - %s' % (self.id, self.entrada.produto.descricao)


from django.db.models.signals import post_save, post_delete
from signals import update_quantidade, delete_quantidade, efetua_baixa
post_save.connect(update_quantidade, sender=Entrada)
post_delete.connect(delete_quantidade, sender=Entrada)
post_save.connect(efetua_baixa, sender=Baixa)

