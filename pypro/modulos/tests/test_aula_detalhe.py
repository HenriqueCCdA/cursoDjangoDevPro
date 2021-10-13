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


def test_video(resp, aula: Aula):
    assert_contains(resp, f'"https://www.youtube.com/embed/{aula.youtube_id}"')


def test_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')
