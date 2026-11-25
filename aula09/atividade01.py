#lista de contatos
#registrar dados de 3 contatos
#nome completo, telefone e e-mail
#ao final apresentar todos os contatos cadastrados para consulta

lista_contatos = []

for i in range(3):
    print(f'\nContato {i+1}')
    contato = {}

    contato['nome'] = input(f'Informe o nome completo: ')
    contato['telefone'] = int(input(f'Informe o telefone: '))
    contato['email'] = input(f'Informe o e-mail: ')

    lista_contatos.append(contato)

for contato in lista_contatos:
    print(f'Nome Completo: {contato['nome']}') 
    print(f'Telefone: {contato['telefone']}')
    print(f'E-mail: {contato['email']}')

