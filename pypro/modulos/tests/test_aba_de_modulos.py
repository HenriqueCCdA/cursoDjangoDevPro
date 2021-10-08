import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.base.django_assertions import assert_contains
from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2)


@pytest.fixture
def resp(client, modulos):
    response = client.get(reverse('base:home'))
    return response


def test_titulos_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_link_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.get_absolute_url())
