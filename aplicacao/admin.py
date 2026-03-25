from django.contrib import admin

from .models import Produto, Perfil, Venda, ItemVenda


@admin.register(Produto)
class ProdutoAdm(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'qtde', 'descricao','data','imagem')
    list_display_links = ('nome',)
    search_fields = ('nome', 'qtde')
    list_filter = ('preco', 'qtde')
    list_editable = ('preco', 'qtde')



@admin.register(Perfil)
class PerfilAdm(admin.ModelAdmin):
    list_display = ('id', 'telefone', 'bairro', 'numero', 'cidade',)



@admin.register(Venda)
class VendaAdm(admin.ModelAdmin):
    list_display = ('id', 'data',)


@admin.register(ItemVenda)
class ItemVendaAdm(admin.ModelAdmin):
    list_display = ('id', 'qtde',)

