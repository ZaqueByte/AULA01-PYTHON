from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produto
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import UsuarioForm

def index(request):
    context = {'curso': 'Desenvolvimento de Sistemas'}
    return render(request, 'index.html', context)

def contatos(request):
    context = {'telefone' : '2050-2050', 'email' : 'carlinhos@gmail.com'}
    return render(request, 'contatos.html', context)

@login_required(login_url="urlentrar")
def produto(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request,"produto.html", context)

def cadastrarProduto(request):
    return render(request, "cadastrarProduto.html")

def salvarProduto(request):
    thisnome = request.POST.get('txtNome')
    thispreco = request.POST.get('txtPreco')
    thisqtde = request.POST.get('txtQtde')
    thisdata = request.POST.get('txtData')
    thisdescricao = request.POST.get('txtDescricao')
    
    preco_formatado = thispreco.replace('.','').replace(',','.')

    produto = Produto(
        nome = thisnome,
        preco = float(preco_formatado),
        qtde = thisqtde,
        data = thisdata,
        descricao = thisdescricao
    )

    produto.save()
    return redirect('urlproduto')

def editarProduto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == "GET":
        context = {'p': produto}
        return render(request, "editarProduto.html", context)
    else:
        produto.nome = request.POST.get('txtNome')
        produto.preco = request.POST.get('txtPreco').replace(',','.')
        produto.qtde = request.POST.get('txtQtde')
        data_string = request.POST.get('txtData')
        if data_string:
            produto.data = datetime.strptime(data_string, '%Y-%m-%d').date()
        produto.descricao = request.POST.get('txtDescricao')

        produto.save()
        return redirect('urlproduto')

def excluirProduto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        produto.delete()
        return redirect('urlproduto')
    return render(request, "excluirProduto.html", {"p": produto})

def entrar(request):
    if request.method == "GET":
        return render (request,"entrar.html")
    elif request.method == "POST":
        usuario = request.POST.get("txtUser")
        senha = request.POST.get("txtPass")
        user = authenticate(username=usuario, password=senha)

        if user:
            login(request,user)
            return redirect('urlproduto')
        messages.error(request, "Falha na autenticação!")
        return render(request,'entrar.html')
    
def sair(request):
    logout(request)
    return redirect('urlentrar')

def cadastrarUsuario(request):
    if request.method == "GET":
        form = UsuarioForm()
        context = {'form' : form}
        return render (request, 'cadastrarUsuario.html', context)
    else:
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('urlentrar')