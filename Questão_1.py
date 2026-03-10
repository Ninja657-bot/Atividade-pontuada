import os
os.system("cls")

numeroA = int(input("Digite um número: "))
numeroB = int(input("Digite outro número: "))
numeroC = int(input("Digite mais um número: "))

soma = numeroA + numeroB
print(f"{numeroA} + {numeroB} = {soma}")

if soma > numeroC: 
    print(f"A soma dos dois primeiros números ({numeroA} + {numeroB} = {soma}) é maior que o terceiro ({numeroC}).")
else:
    print(f"O terceiro número ({numeroC}) digitado é maior que a soma dos dois primeros ({numeroA} + {numeroB} = {soma}).")