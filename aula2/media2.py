nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
media = (nota1+nota2+nota3)/3
print(f"A média das suas notas é {media}")

if media > 7:
    print("Você passou, parabéns!")
else:
    print("Boa sorte na recuperação.")