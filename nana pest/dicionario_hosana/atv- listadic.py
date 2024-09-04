def adicionar_produtos(produtos : dict, produto: str, dados : dict):
    produtos[produto] = dados

def excluir_produtos(produtos : dict, produto : dict):
    produtos.pop(produto)


def atulizar_preço(produtos : dict, produto: str, novo_preco : float, chave_atual ):
    produtos[produto[chave_atual]] = novo_preco

produtos = {
    "Vodka" : {'categoria' : 'Bebida', 'preco': 50},
    "Pizza" : {'categoria' : 'Comida', 'preco': 35},
    "Detergente" : {'categoria' : 'Limpeza', 'preco': 2},
    "Laranja" : {'categoria' : 'Frutas', 'preco': 5.2}
}


    
