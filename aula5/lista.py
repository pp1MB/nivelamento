tamanho = 0
lista = []

while tamanho <= 0:
    try:
        tamanho = int(input("Digite o tamanho da lista: "))

        if tamanho <= 0:
            print("Valor Inválido.")
        else:
            break
    except:
        print("Valor Inválido.")

while len(lista) < tamanho:
    try:
        lista.append(float(input(f"Digite o número {(len(lista)+1)}: ")))
    except:
        print("Valor Inválido.")

print(lista)
print(f"O valor máximo é {max(lista)} e o valor mínimo é {min(lista)}.")

lista.sort()
print(f"Ordem crescente: {lista}")

lista.reverse()
print(f"Ordem decrescente: {lista}")