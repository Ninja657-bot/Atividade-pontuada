import os
os.system("cls")

numeroA = int(input("Digite um número: "))
numeroB = int(input("Digite outro número: "))
if numeroA == numeroB:
    numeroC = numeroA + numeroB
    print(f"A soma dos dois números é {numeroC}")
else: 
    numeroC = numeroA * numeroB
    print(f"O produto dos números é {numeroC}")