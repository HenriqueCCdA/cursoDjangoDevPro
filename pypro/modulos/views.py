from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pypro.modulos import facade


def indice(request):
    ctx = {'modulos': facade.listar_modulos_com_aulas()}
    return render(request, 'modulos/indice.html', context=ctx)


def detalhe(request, slug):
    modulo = facade.encontar_modulo(slug)
    aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', context={'modulo': modulo, 'aulas': aulas})


@login_required
def aula(request, slug):
    aula = facade.encontar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', context={'aula': aula})
