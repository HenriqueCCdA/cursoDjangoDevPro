from django.shortcuts import render

from pypro.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontar_modulo(slug)
    print(slug, modulo)

    return render(request, 'modulos/modulo_detalhe.html', context={'modulo': modulo})
