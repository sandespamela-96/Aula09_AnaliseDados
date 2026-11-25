#funções
#print()
#input()
#int()

#definindo a função
def saudacao():
    print('Olá!')

def saudacao2(x): # x é um parametro na função
    print(f'Olá! {x}')

# saudacao()
# saudacao()
# saudacao()
#--------------------------------
nome = input('Nome: ')
saudacao2(nome) #passagem por parametro
saudacao2('Antonio')
saudacao2('Pedro')
