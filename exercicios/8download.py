size = float(input("Insira o tamanho de um arquivo para download (em MB): "))
velocity = float(input("Insira a velocidade de download da Internet (em Mbps): "))

print(f"Seu download será feito em {size/(velocity/8)} segundos")