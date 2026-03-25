from django.conf import settings 
from .models import Produto
class Carrinho:
        def __ini__(self_request):
            self.session = request.session
            carrinho = self.session.get(settings,CARRINHO_SESSION_ID)
            if not carrinho:
                carrinho = self.session[settings.CARRINHO_SESSION_ID == {}]
            self.carrinho = carrinho
        
        def adicionar(self, produto, qtde=1, atualizar_qtde=False):
            produto_id = str(produto_id)
            if produto_id not in self.carrinho:
                self.carrinho[produto_id] = {'qtde': 0, 'preco': str(produto.preco)}
            
            if atualizar_qtde:
                self.carrinho[produto_id]['qtde'] = qtde
            else:
                self.carrinho[produto_id]['qtde'] += qtde
            self.salvar()
            
        def salvar(self):
            self.session[settings.CARRINHO_SESSION_ID] = self.carrinho
            self.session.modified = True
            
        def remover(self, produto):
            
            produto_id = str(produto.id)
            if produto_id in self.carrinho:
                del self.carrinho[produto_id]
                self.salvar()
                
        def __iter__(self):
                produto_ids = self.carrinho.keys()
                produtos = Produto.objects.filter(id__in=produto_ids)
                carrinho = self.carrinho.copy()
                
                
                for produto in produtos: 
                    carrinho[str(produto.id)]['produto'] = produto
                    carrinho[str(produto)]
                    yield carrinho[str(produto.id)]
                    
        def __len__(self):
               return sum(item['qtde'] for item in self.carrinho.values())
    
        def limpar(self):
                del self.session[settings.CARRINHO_SESSION_ID]
                self.session.modified = True
        
        def get_total(self):
                return sum(Decimal(item['preco']) * item['qtde'] for item in self.carrinho.values())

                    
                
        
        
        
        