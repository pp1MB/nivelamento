number1 = float(input("Insira um número: "))
number2 = float(input("Insira um segundo número: "))
number3 = float(input("Insira um terceiro número: "))

if number1 > number2 and number1 > number3:
    print(f"O número {number1} é o maior.")
elif number2 > number1 and number2 > number3:
    print(f"O número {number2} é o maior.")
elif number3 > number1 and number3 > number2:
    print(f"O número {number3} é o maior.")
else:
    print("Todos os números são iguais.")