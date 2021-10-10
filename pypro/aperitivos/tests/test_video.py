import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.aperitivos.models import Video
from pypro.base.django_assertions import assert_contains


@pytest.fixture
def video(db):
    return baker.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug+'nao_existe',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_status_code_video_nao_emcontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp, video):
    assert_contains(resp, f'<iframe src="https://www.youtube.com/embed/{video.youtube_id}"')
