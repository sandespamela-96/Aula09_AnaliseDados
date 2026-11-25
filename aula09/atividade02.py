def dobro(x):
    res = x * 2
    return res

# n = float(input(f'Infome um número: '))
# resultado = dobro(n)
# print(f'O dobro é {resultado}')

def triplo(y):
    res = y * 3
    return res

# n = float(input(f'Infome um número: '))
# resultado = triplo(n)
# print(f'O dobro é {resultado}')

def quadrado(z):
    res = z ** 2
    return res

n = float(input(f'Infome um número: '))
resultado1 = dobro(n)
resultado2 = triplo(n)
resultado3 = quadrado(n)

print(f'\nO dobro é {resultado1}')
print(f'O triplo é {resultado2}')
print(f'O quadrado é {resultado3}')