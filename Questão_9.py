import os 
os.system("cls")

name = input("Digite seu nome: ")
renda = float(input(f"Olá {name} digite o valor da sua renda mensal: "))
valor = float(input("Quanto o senhor deseja: "))
quantidade = int(input("""Em quantos messes o senhor pretende pagar ?
"""))

#Calculos
prestacao = valor / quantidade
valormax = renda * 10
valorprestacaomin = renda * (30 / 100)

#Resposta

if valor > valormax or valorprestacaomin < prestacao:
    print("Infelizmente o senhor não pode prosseguir com o emprestimo.")
else: 
    print("O pedido de emprestimo pode prosseguir")
    print(f"""Valor total: {valor:.2f}
Prestações: {quantidade}
Valor das prestações: {prestacao:.2f}
""")