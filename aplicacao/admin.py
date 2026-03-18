from django.contrib import admin

from .models import Produto, Cliente, Perfil, Venda, itemVenda

@admin.register(Produto)
class ProdutoAdm(admin.ModelAdmin):
    list_display = ('id','nome', 'preco','qtde','data')
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('preco', 'qtde')
    list_editable = ('preco', 'qtde')

@admin.site.register(Perfil)
class PerfilAdm(admin.ModelAdmin):
    list_display = ('id','')
