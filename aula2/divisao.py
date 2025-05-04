number = int(input("Escreva um número inteiro:"))

if number%2 == 0:
    print("Fizz")

if number%5 == 0:
    print("Buzz")

if number%2 != 0 and number%5 != 0:
    print("nenhum")