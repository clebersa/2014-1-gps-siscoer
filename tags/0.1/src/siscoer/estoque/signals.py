#coding:utf-8


def update_quantidade(instance, created, *args, **kwargs):
    if created:
        instance.produto.quantidade += instance.quantidade
        instance.produto.save()
    else:
        if instance.produto.quantidade <= 0:
            instance.produto.quantidade = 0
            instance.produto.save()


def delete_quantidade(instance, *args, **kwargs):
    instance.produto.quantidade -= instance.quantidade
    instance.produto.save()


def efetua_baixa(instance, created, *args, **kwargs):
    if created:
        if instance.quantidade <= instance.entrada.quantidade:
            instance.entrada.quantidade -= instance.quantidade
            instance.entrada.save()

            instance.entrada.produto.quantidade -= instance.quantidade
            instance.entrada.produto.save()
        else:
            instance.entrada.quantidade = 0
            instance.entrada.save()

            instance.entrada.produto.quantidade -= instance.quantidade
            instance.entrada.produto.save()

        if instance.entrada.quantidade <= 0:
            instance.entrada.quantidade = 0
            instance.entrada.finalizado = True
            instance.entrada.save()

