menuinicial = '''
Bem vindo à Calculadora!
------------------------------
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
------------------------------
'''

interface = '''
------------------------------
Escolha uma das opções disponíveis:
1 - Soma / 2 - Subtração / 3 - Multiplicação / 4 - Divisão
------------------------------
'''

print(menuinicial)
while True:
    try:
        escolha = int(input("Escolha uma operação:"))
        if escolha not in range(1,5):
            print(interface)
        else:
            number1 = int(input("Digite o primeiro número:"))
            number2 = int(input("Digite o segundo número:"))

            if escolha == 1:
                result = number1 + number2
                carater = "soma"
            elif escolha == 2:
                result = number1 - number2
                carater = "subtração"
            elif escolha == 3:
                result = number1 * number2
                carater = "multiplicação"
            elif escolha == 4:
                result = number1 / number2
                carater = "divisão"
            
            print("-"*30)
            print(f"O resultado da {carater} é {result}.")
            print(interface)
    except ZeroDivisionError:
        print("-"*30)
        print("Divisão por zero é indefinido.")
        print(interface)
    except:
        print("-"*30)
        print("Valor Inválido.")
        print("-"*30)