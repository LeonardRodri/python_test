produto = {'nome': 'Caneta', 'preco': 14.99,
           'importado': True, 'estoque': 793}

for chave in produto.keys():
    print(f'{chave}')

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f'{chave} = {valor}')