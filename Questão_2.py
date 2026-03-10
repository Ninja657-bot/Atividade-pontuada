import os
os.system("cls")

nome = input("Digite seu nome: ")
sexo = (input("Qual seu sexo (Escreva F ou M): "))
estado = (input("Estado civil: "))

if sexo == "F" and estado == "Casada":
    sexo = "Feminino"
    print()
    tempo = int(input("""Quantos anos tem casada ?
"""))    
    print()
    print("- Gerando ficha -")
    print()
    print(f"Nome: {nome}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estado}")
    print(f"Tempo de casamento: {tempo}") 
else:
    if sexo == "M":
        sexo = "Masculino"
    if sexo == "F":
        sexo = "Feminino"
    print()
    print("- Gerando ficha -")
    print()
    print(f"Nome: {nome}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estado}") 