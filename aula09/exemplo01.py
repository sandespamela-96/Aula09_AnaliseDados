produto1 = {} # Dicionário vazio

produto = {
    'nome': 'Notebook',
    'preco': 3500.80,
    'marca': 'Lenovo'
}

# print(type(produto))
print(produto) #todas as chaves e valores

print(produto['nome']) #chave nome
print(produto['preco']) #chave preço

# Alterando o valor
produto['marca'] = 'Positivo'
print(produto['marca'])

# Adicionando chaves
produto['tela'] = '18"'
print(produto)

# Deletando uma chave
del produto['marca']
print(produto)

print(produto.keys()) #chaves
print(produto.values()) #valores
print(produto.items()) # transforma em lista