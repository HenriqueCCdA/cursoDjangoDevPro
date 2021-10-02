import pytest
from django.urls import reverse
from pypro.base.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    response = client.get(reverse('base:home'))
    return response


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Python Pro - Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro</a>')
