from django.urls import path
from .views import index, contatos, produto, cadastrarProduto, salvarProduto, editarProduto, excluirProduto

urlpatterns = [
    path('', index, name="urlindex"),
    path('contatos/', contatos, name="urlcontatos"),
    path('produto/', produto, name="urlproduto"),
    path('cadastrarProduto/', cadastrarProduto, name="urlcadastrarProduto"),
    path('salvarProduto/', salvarProduto, name="urlsalvarProduto"),
    path('editarProduto/<int:id>/', editarProduto, name="urleditarProduto"),
    path('excluirProduto/<int:id>/', excluirProduto, name="urlexcluirProduto"),
]