import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.base.django_assertions import assert_contains
from pypro.modulos.models import Modulo


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def resp(client, modulo: Modulo):
    response = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return response


def test_titulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)


def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)
