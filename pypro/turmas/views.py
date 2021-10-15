from django.shortcuts import render

# Create your views here.


def indice(request):
    return render(request, 'turmas/indice.html')
