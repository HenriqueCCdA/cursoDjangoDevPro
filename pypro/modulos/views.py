from django.shortcuts import render

from pypro.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontar_modulo(slug)
    aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', context={'modulo': modulo, 'aulas': aulas})


def aula(request, slug):
    aula = facade.encontar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', context={'aula': aula})
