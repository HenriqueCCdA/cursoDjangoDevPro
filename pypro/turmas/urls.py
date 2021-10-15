from django.urls import path

from pypro.turmas.views import indice

app_name = 'turmas'
urlpatterns = [
    path('',  indice, name='indice'),
]
