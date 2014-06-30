#coding:utf-8
from django.contrib.auth.models import User, Group

def update_user(instance, created, *args, **kwargs):
    if created:
        usuario = User()
        usuario.username = instance.login
        usuario.set_password(instance.senha)
        usuario.first_name = instance.login[0]
        usuario.email = instance.mail
        usuario.is_staff = True
        usuario.is_active = True
        usuario.save()

        instance.user = usuario
        instance.save()
    else:
        usuario = User.objects.get(id=instance.user.id)
        usuario.username = instance.login
        usuario.set_password(instance.senha)
        usuario.first_name = instance.login[0]
        usuario.email = instance.mail
        usuario.is_staff = True
        usuario.is_active = True
        usuario.save()