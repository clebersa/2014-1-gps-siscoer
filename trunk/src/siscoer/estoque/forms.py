#coding:utf-8
from django.core.exceptions import ValidationError
from django.forms import Form, ModelChoiceField, CharField, ModelForm, ChoiceField, EmailField, \
    TextInput, Select, DateField, DateInput, BooleanField, URLField, DecimalField, Textarea, DateTimeField, TimeField, \
    TimeInput, IntegerField, PasswordInput
from usuario.models import Usuario
from models import Localizacao, Categoria, Produto, Entrada, Baixa


class CadastroExternoForm(Form):
    class Meta:
        model = Usuario
    login = CharField(label=(u'Login'), max_length=30, required=True, widget=TextInput(attrs={'class' : 'form-control'}))
    senha = CharField(label=(u'Senha'), max_length=30, required=True, widget=PasswordInput(attrs={'class' : 'form-control'}))
    mail = EmailField(max_length=200, label=u'Email', required=True, widget=TextInput(attrs={'class' : 'form-control'}))
    pergunta = CharField(max_length=250, required=True, label=u'Pergunta Secreta', widget=TextInput(attrs={'class' : 'form-control'}))
    resposta = CharField(max_length=250, required=True, label=u'Resposta Secreta', widget=TextInput(attrs={'class' : 'form-control'}))

    def clean_mail(self):
        email_principal = self.cleaned_data['mail']
        if Usuario.objects.filter(mail=email_principal).exists():
            raise ValidationError(u"E-mail já existe")
        return email_principal


class PerfilForm(ModelForm):
    class Meta:
        model = Usuario
        exclude = ('user','indicador','indicador_original','slug','saque','isento_ir','cpf_cnpj','tipo_pessoa','razao_social','nome_responsavel','insc_estadual','insc_municipal','aceite','obs','receber_email','status','data_cancelamento',)
    login = CharField(label=(u'Login'), max_length=30, required=True, widget=TextInput(attrs={'class' : 'form-control'}))
    senha = CharField(label=(u'Senha'), max_length=30, required=True, widget=PasswordInput(attrs={'class' : 'form-control'}))
    mail = EmailField(max_length=200, label=u'Email', required=True, widget=TextInput(attrs={'class' : 'form-control'}))
    pergunta = CharField(max_length=250, required=True, label=u'Pergunta Secreta', widget=TextInput(attrs={'class' : 'form-control'}))
    resposta = CharField(max_length=250, required=True, label=u'Resposta Secreta', widget=TextInput(attrs={'class' : 'form-control'}))


class CadastroEstoqueForm(Form):
    class Meta:
        model = Localizacao
    descricao = CharField(label=(u'Identificação'), help_text=u'Digite o nome do Estoque ou Localização.' , max_length=100, required=True, widget=TextInput(attrs={'class' : 'form-control'}))


class CadastroCategoriaForm(Form):
    class Meta:
        model = Categoria
    descricao = CharField(label=(u'Categoria'), help_text=u'Digite o nome da Categoria.' , max_length=100, required=True, widget=TextInput(attrs={'class' : 'form-control'}))


class CadastroProdutoForm(Form):
    UNIDADE = (
        (0,(u'Unidade')),
        (1,(u'Litro(s)')),
        (2,(u'Metro(s)')),
        (3,(u'Quilograma(s)')),
    )
    class Meta:
        model = Produto
    categoria = ModelChoiceField(Categoria.objects.all(), required=True, widget=Select(attrs={'class' : 'form-control'}))
    descricao = CharField(label=(u'Descrição'), help_text=u'Digite o nome do Produto.' , max_length=150, required=True, widget=TextInput(attrs={'class' : 'form-control'}))
    unidade = ChoiceField(choices=UNIDADE, label=u'Unidade', required=True, widget=Select(attrs={'class' : 'form-control'}))


class CadastroEntradaForm(Form):
    class Meta:
        model = Entrada
    localizacao = ModelChoiceField(Localizacao.objects.all(), required=True, widget=Select(attrs={'class' : 'form-control'}))
    produto = ModelChoiceField(Produto.objects.all(), required=True, widget=Select(attrs={'class' : 'form-control'}))
    quantidade = IntegerField(required=True, widget=TextInput(attrs={'class' : 'form-control'}))
    validade = DateField(label=u'Data Validade', help_text=u'Ex.: 01/01/1990', required=True, widget=DateInput(format='%d/%m/%Y', attrs={'class' : 'form-control'}))
    valor = DecimalField(label=u'Valor em R$', localize=True, widget=TextInput(attrs={'class' : 'form-control'}))
    local_compra = CharField(label=(u'Local Compra'), help_text=u'Ex.: Supermercado Bretas' , max_length=150, required=True, widget=TextInput(attrs={'class' : 'form-control'}))
    data_compra = DateField(label=u'Data Compra', help_text=u'Ex.: 01/01/1990', required=True, widget=DateInput(format='%d/%m/%Y', attrs={'class' : 'form-control'}))


class CadastroBaixaForm(Form):
    MOTIVO = (
        (0,(u'Consumiu')),
        (1,(u'Estragou')),
        (2,(u'Doação')),
        (3,(u'Outro(s)')),
    )
    class Meta:
        model = Baixa
    entrada = ModelChoiceField(Entrada.objects.all().exclude(quantidade=0), label=u'Produto em Estoque', required=True, widget=Select(attrs={'class' : 'form-control'}))
    quantidade = IntegerField(label=u'Quantidade para Baixar' , required=True, widget=TextInput(attrs={'class' : 'form-control'}))
    motivo = ChoiceField(choices=MOTIVO, label=u'Motivo', required=True, widget=Select(attrs={'class' : 'form-control'}))





