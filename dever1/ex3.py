first = int(input("Insira o primeiro número inteiro: "))
second = int(input("Insira o segundo número inteiro: "))

result = first%second == 0 or second%first == 0
print(f"{first} e {second} são múltiplos? {result}")