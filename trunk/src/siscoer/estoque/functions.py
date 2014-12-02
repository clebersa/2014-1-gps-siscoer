#coding:utf-8
import random
import string
import time
from django.core.mail import send_mail


#################################
### Settings to Mail
#################################
DEFAULT_FROM_EMAIL = 'SISCOER <siscoer@weslleyaraujo.com>'
SERVER_EMAIL = 'mail.weslleyaraujo.com'
EMAIL_HOST_USER = 'siscoer@weslleyaraujo.com'
EMAIL_HOST_PASSWORD = '$dc@tHuz&28'
EMAIL_SUBJECT_PREFIX = '[SISCOER]'
EMAIL_HOST = 'mail.wesllearaujo.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#################################
### End Settings
#################################


def gen_pass(size=16):
    """
    Descrição: gera uma senha aleatória do tamanho especificado.
    """
    chars = []
    chars.extend([i for i in string.ascii_letters])
    chars.extend([i for i in string.digits])
    chars.extend([i for i in '\'"!@#$%&*()-_=+[{}]~^,<.>;:/?'])
    passwd = ''

    for i in range(size):
        passwd += chars[random.randint(0,  len(chars) - 1)]

        random.seed = int(time.time())
        random.shuffle(chars)

    return passwd


def request_user_pass(instance, *args, **kwargs):
    new_pass = gen_pass()
    try:
        titulo = 'Recuperar Senha - SISCOER'
        destino = instance.mail
        texto = u"""
        Olá %s!

        Segue abaixo seus dados de usuário e senha para acesso ao sistema:

        Endereço: https://siscoer.weslleyaraujo.com/login
        Usuário: %s
        Nova senha: %s
        (Troque sua senha o mais breve possível para sua segurança.)

        Equipe SISCOER
        """ % (instance.login, instance.login, new_pass)

        send_mail(
            subject=titulo,
            message=texto,
            from_email=EMAIL_HOST_USER,
            recipient_list=[destino],
        )
    except:
        pass
