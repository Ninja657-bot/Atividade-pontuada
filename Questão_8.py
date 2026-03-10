import os 
os.system("cls")

cor = input("Qual a cor do CD escolhido: ")
match cor:
    case "Verde":
        valor = 10.00
    case "Azul":
        valor = 20.00
    case "Amarelo":
        valor = 30.00
    case "Vermelho":
        valor = 40.00
    case _:
        print("Cor invalida")
        exit()
        
print(f"O CD de {cor} é R${valor}")