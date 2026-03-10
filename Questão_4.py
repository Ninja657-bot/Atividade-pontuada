import os
os.system("cls")

name = input("Digite seu nome: ")

print("""          |    Até 5 Kg    |   Acima de 5 Kg  |
          Morango  | R$2,50 por Kg  |   R$2,20 por Kg  |
            Maçã   | R$1,80 por Kg  |   R$1,50 por Kg  |
""")
valormorango = 2.50
valormaça = 1.80     
quantidade1 = int(input(f"""{name}, quantos morangos ira querer hoje ?
"""))
if quantidade1 >= 5:
    valormorango = 2.20
valor1 = valormorango * quantidade1
if quantidade1 >= 10 or valor1 >= 15:
    valortotal = valor1 * (1 - 10 / 100)
else:
    valortotal = valor1
print(f"Você escolheu {quantidade1} morangos")
input(f"Fica no valor de {valortotal:.2f}") 
print()

quantidade2 = int(input(f"""Quantas mmaçãs ira querer {name} ?
"""))
if quantidade2 >= 5:
    valormaça = 1.50
valor2 = valormaça * quantidade2
if quantidade2 >= 10 or valor2 >= 15:
    valortota2 = valor2 * (1 - 10 / 100)
else:
    valortotal2 = valor2
print(f"Você escolheu {quantidade2} maçãs")
input(f"Fica no valor de {valortotal2:.2f}")

print(f"Serão {quantidade1} morangos e {quantidade2} maçãs.")
print(f"Valor total dos Morangos: {valortotal}")
print(f"Valor total das Maçãs: {valortota2}")
soma = valortotal + valortota2
print(f"Total: {soma}")     