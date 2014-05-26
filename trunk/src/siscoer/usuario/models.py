#coding:utf-8
from django.core.urlresolvers import reverse
from django.db.models import Model, CharField, ForeignKey, EmailField, DateTimeField
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Usuario(Model):
    class Meta:
        verbose_name = _(u'Usuário')
        verbose_name_plural = _(u'Usuários')
        app_label = 'usuario'
    user = ForeignKey(User, verbose_name=_(u'Usuário'), blank=True, null=True,)
    login = CharField(verbose_name=_(u'Login'), max_length=30, help_text=_(u'Usuário para login'))
    senha = CharField(verbose_name=_(u'Senha'), max_length=30, help_text=_(u'Senha para login'))
    mail = EmailField(verbose_name=_(u'Email'), max_length=200, help_text=_(u'Email válido'))
    pergunta = CharField(verbose_name=_(u'Pergunta Secreta'), max_length=250, help_text=_(u'Digite a pergunta secreta.'))
    resposta = CharField(verbose_name=_(u'Resposta Secreta'), max_length=250, help_text=_(u'Digite a resposta secreta'))
    cadastro = DateTimeField(verbose_name=_(u'Data de Cadastro'), auto_now_add=True, editable=False)
    alteracao = DateTimeField(verbose_name=_(u'Data de Alteração'), auto_now=True, editable=False)

    def __unicode__(self):
        return u'%s' % self.login

    def get_link_usuario(self):
        return '%s' % reverse('admin:usuario_usuario_change', args=[self.pk])

from signals import update_user
post_save.connect(update_user, sender=Usuario)