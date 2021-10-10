from typing import List

from pypro.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por títulos
    :return:
    """
    return list(Modulo.objects.order_by('order').all())


def encontar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)
