Positivos = 0
Negativos = 0

for i in range(0,3):
    N = int(input("Digite um número: "))
    if N > 0:
        Positivos = Positivos + N
    if N < 0:
        Negativos = Negativos + 1
print(f"A soma de números positivos é {Positivos}")
print(f"A quantidade de números negativos é {Negativos}")
