lista_catalogo = []

for i in range(3):
    print(f'\nLivro {i+1}')
    livro = {}

    livro['titulo'] = input('Informe o nome do livro: ')
    livro['autor'] = input('Informe o nome do autor: ')
    livro['ano'] = int(input('Informe o ano de publicação: '))
    livro['genero'] = input('Informe o gênero: ')
    livro['paginas'] = int(input('Informe o número de páginas: '))

    lista_catalogo.append(livro) #adicionar todas informações na lista

# print(lista_catalogo)

for elemento in lista_catalogo: # vai rodar na quantidade de elementos (range) que tem na lista
    # print(elemento) #teste para o for
    if elemento['ano'] >= 2020:
        # print(elemento) # todas as informações da lista
        print(f'\nLivro {i+1}')
        print(f'Nome: {elemento['titulo']}') #retorna somente o valor desejado
        print(f'Ano: {elemento['ano']}') #retorna somente o valor desejado
