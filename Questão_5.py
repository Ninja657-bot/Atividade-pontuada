import os
os.system("cls || clear")

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite o segundo número: "))
operação = (input("Coloque a operação a ser feita: "))
resultado = float
match operação:
    case "+":
        resultado = numero_1 + numero_2 
        print(f"{numero_1} + {numero_2} = {resultado}")
    case "-":
        resultado = numero_1 - numero_2
        print(f"{numero_1} - {numero_2} = {resultado}")
    case "X":
        resultado = numero_1 * numero_2
        print(f"{numero_1} * {numero_2} = {resultado:.f}")
    case "/": 
        resultado = numero_1 / numero_2
        print(f"{numero_1} / {numero_2} = {resultado:.f}")
    case _:
        print("Dados incorretos")
        resultado =0
        
print(f"Resultado: {resultado}")
print()
print("==== Fim ====")