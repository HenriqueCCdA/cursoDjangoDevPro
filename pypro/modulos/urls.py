from django.urls import path

from pypro.modulos.views import detalhe

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', detalhe, name='detalhe'),
]
