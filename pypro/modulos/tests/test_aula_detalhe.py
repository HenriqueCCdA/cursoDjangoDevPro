import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.base.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    response = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return response


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)
