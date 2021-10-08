from pypro.modulos import facade


def listar_modulos(request):
    return {'MODULO': facade.listar_modulos_ordenados()}
