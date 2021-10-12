from django.urls import path

from pypro.modulos.views import detalhe, aula

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', detalhe, name='detalhe'),
    path('aulas/<slug:slug>', aula, name='aula'),
]
