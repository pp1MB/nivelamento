gainhour = float(input("Insira o seu ganho por hora trabalhada: "))
hours = float(input("Insira o número de horas trabalhadas por mês: "))

salary = gainhour*hours
IR = salary*(0.11)
INSS = salary*(0.08)
Sindicato = salary*(0.05)

print("//RECEITA FEDERAL//")
print(f"+ Salário Bruto: R${salary}")
print(f"- IR: R${IR}")
print(f"- INSS: R${INSS}")
print(f"- Sindicato: R${Sindicato}")
print("------------")
print(f"Salário Líquido: R${salary-IR-INSS-Sindicato}")