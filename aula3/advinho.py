from random import randint
numeroAleatorio = randint(1, 20)
escolha = 0
tentativas = 0

while numeroAleatorio != escolha and tentativas < 5:
    escolha = int(input("Escolha um número de 1 a 20: "))
    
    if escolha > numeroAleatorio:
        print("O número é menor que esse.")
    if escolha < numeroAleatorio:
        print("O número é maior que esse.")
    tentativas +=1

if numeroAleatorio == escolha:
    print(f"Você acertou! Você precisou de {tentativas} tentativas.")
elif tentativas == 5:
    print("Que pena! Você excedeu o número de tentativas.")