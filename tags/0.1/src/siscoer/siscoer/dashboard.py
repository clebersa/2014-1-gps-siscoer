#coding:utf-8
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        ### append a group for "Administration" & "Applications"
        # self.children.append(modules.Group(
        #     _(u'ALL'),
        #     column=1,
        #     collapsible=True,
        #     css_classes=('grp-collapse grp-closed',),
        #     children = [
        #         modules.AppList(
        #             title=_(u'Configurações'),
        #             column=1,
        #             collapsible=True,
        #             models=('*',)
        #         )
        #         ]
        # ))

        # self.children.append(modules.AppList(
        #     _(u'1 - Grupos, Usuários e Permissões'),
        #     collapsible=True,
        #     column=1,
        #     css_classes=('grp-collapse grp-closed',),
        #     models=('django.contrib.*',),
        #     ))

        self.children.append(modules.AppList(
            _(u'1 - Usuários'),
            collapsible=True,
            column=1,
            css_classes=('grp-collapse grp-opened',),
            models=('usuario.*',),
            ))

        self.children.append(modules.AppList(
            _(u'2 - Estoque'),
            collapsible=True,
            column=1,
            css_classes=('grp-collapse grp-opened',),
            models=('estoque.*',),
            ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _(u'Recent Actions'),
            column=2,
            limit=7,
            collapsible=True,
            ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _(u'Suporte e Informações'),
            column=2,
            children=[
                {
                    'title': _(u'Ajuda SISCOER'),
                    'url': 'http://ajuda.siscoer.com.br/',
                    'external': True,
                },
            ]
        ))

        



