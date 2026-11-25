def soma(x, y):
    r = x + y
    # print(r)
    return r #retorna o resultado para quem chamou


# soma(5, 9)

#num1 = 5
#num2 = 9
#soma(num1, num2)

for i in range(3):
    num1 = float(input('Informe um número: '))
    num2 = float(input('Informe outro número: '))
    resultado = soma(num1, num2) #chamada da função
    print(resultado)
