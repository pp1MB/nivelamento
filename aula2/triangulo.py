lado1 = int(input("Insira o lado 1: "))
lado2 = int(input("Insira o lado 2: "))
lado3 = int(input("Insira o lado 3: "))

if (lado1+lado2)>lado3 and (lado1+lado3)>lado2 and (lado2+lado3)>lado1:
    print("Os valores atribuídos podem formar um triângulo.")
    if lado1 == lado2 == lado3:
        print("Seu triângulo é equilátero.")
    elif lado1 == lado2 or  lado1 == lado3 or lado2 == lado3:
        print("Seu triângulo é isósceles.")
    else:
        print("Seu triângulo é escaleno.")
else:
    print("Os valores atribúidos NÃO podem formar um triângulo.")