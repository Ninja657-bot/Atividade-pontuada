import os
os.system("cls")

precoA = float(3.79)
precoG = float(6.59)

name = input("Digite seu nome: ")
tipo = input("Digite ao tipo de combustível (A-álcoold/G-Gasolina): ").upper()
litros = float(input("Quantos litros: "))


match tipo:
    case "A":
        if litros <= 25:
            valor = precoA * litros
            desconto = valor * (2 / 100)
        else:
            valor = precoA * litros
            desconto = valor * (4 / 100)
    case "G":
        if litros <= 25:
            valor = precoG * litros
            desconto = valor * (3 / 100)
        else:
            valor = precoG * litros
            desconto = valor * (5 / 100)
    case _:
        print("Tipo inválido")
        exit()
print()

if tipo == "A":
    tipo = "Álcool"
if tipo == "G":
    tipo = "Gasolina"

total = valor - desconto
    
print(f"O senhor escolheu {litros}L de {tipo}")
print(f"Total: R${total:.2f}")
print(f"O senhor teve {desconto:.2f} de desconto.")
         