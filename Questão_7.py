import os
os.system("cls")

nome = input("Por favor informe o nome do produto: ")
quantidade = int(input("Quantas unidades está adquirindo: "))
preço = float(input("Qual o valor desse produto: "))

if quantidade <= 5:
    desconto = 2
elif  quantidade > 5 <= 10:
    desconto = 3
elif quantidade > 10:
    desconto = 5
 
    
valor = preço * quantidade
total = valor * (1 - desconto / 100)
economia = valor * (desconto / 100)

print()
print(f"""O senhor está adquirindo {quantidade} unidades do produto {nome}
Pelo valor de: {preço}
Descontos: {desconto}
Valor total: {total:.2f}
O senhor economiza R${economia}
""")