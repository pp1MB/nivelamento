number1 = float(input("Insira um número: "))
number2 = float(input("Insira um segundo número: "))
number3 = float(input("Insira um terceiro número: "))

# Variáveis que vão definir a ordem
first = 0
second = 0
third = 0

# Primeiro da Lista
if number1 > number2 and number1 > number3:
    first = number1
elif number2 > number1 and number2 > number3:
    first = number2
elif number3 > number1 and number3 > number2:
    first = number3

# Terceiro da Lista
if number1 < number2 and number1 < number3:
    third = number1
elif number2 < number1 and number2 < number3:
    third = number2
elif number3 < number1 and number3 < number2:
    third = number3

# Segundo da Lista
if number1 < first and number1 > third:
    second = number1
elif number2 < first and number2 > third:
    second = number2
elif number3 < first and number3 > third:
    second = number3

# Verificação das variáveis
# Se o primeiro for maior que os outros dois 
if first > number1 and first > number2 and number1 == number2:
    second = number1
    third = second
if first > number1 and first > number3 and number1 == number3:
    second = number1
    third = second
if first > number2 and first > number3 and number2 == number3:
    second = number2
    third = second
# Se o terceiro for menor que os outros dois
if third < number1 and third < number2 and number1 == number2:
    first = number1
    second = first
if third < number1 and third < number3 and number1 == number3:
    first = number1
    second = first
if third < number2 and third < number3 and number2 == number3:
    first = number2
    second = first

# Printar a ordem se forem diferentes
if number1 != number2 or number1 != number3:
    print(first, second, third)
else:
    print("Todos os números são iguais.")