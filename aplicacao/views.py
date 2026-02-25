from django.shortcuts import render


def index(request):
    context = {'curso': 'Desenvolvimento de Sistemas'}
    return render(request, 'index.html', context)

def contatos(request):
    context = {'telefone' : '2050-2050', 'email' : 'carlinhos@gmail.com'}
    return render(request, 'contatos.html', context)
# Create your views here.
