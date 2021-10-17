import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.base.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


@pytest.fixture
def usuario(db, django_user_model):
    usuario_modelo = baker.make(django_user_model, email='user')
    senha = 'senha'
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plana = senha
    return usuario_modelo


@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'), {'username': usuario.email,
                                          'password': usuario.senha_plana})


def test_login_form_page(resp):
    assert resp.status_code == 200


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modulos:indice')


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'))


def test_botao_entrar_disponivel(resp_home):
    assert_contains(resp_home, 'Entrar')


def test_link_de_login_disponivel(resp_home):
    assert_contains(resp_home, reverse('login'))


@pytest.fixture
def resp_home_com_usuario_logado(client_com_usuario_logado, db):
    return client_com_usuario_logado.get(reverse('base:home'))


def test_botao_entrar_indisponivel(resp_home_com_usuario_logado):
    assert_not_contains(resp_home_com_usuario_logado, 'Entrar')


def test_link_de_login_indisponivel(resp_home_com_usuario_logado):
    assert_not_contains(resp_home_com_usuario_logado, reverse('login'))


def test_botao_sair_disponive(resp_home_com_usuario_logado):
    assert_contains(resp_home_com_usuario_logado, 'Sair')


def test_nome_usuario_logado_disponive(resp_home_com_usuario_logado, usuario_logado):
    assert_contains(resp_home_com_usuario_logado, usuario_logado.first_name)
