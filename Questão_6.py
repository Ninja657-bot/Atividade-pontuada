import os
os.system ("cls")

nome = input("Por favor digite seu nome: ")
idade = int(input("Agora digite sua idade: "))

valor1 = float(input("Por favor digite a primeira nota: "))
valor2 = float(input("Agora a segunda: "))
valor3 = float(input("E agora a terceira: "))

soma = float( valor1 + valor2 + valor3 )
media = float( soma / 3 )

print("- FICHA DO ALUNO -")
print(f"Nome do aluno: {nome}")
print(f"Idade: {idade}")
print(f"Nota Primeira unidade: {valor1}")
print(f"Nota segunda unidade: {valor2}")
print(f"Nota terceira unidade: {valor3}")
print(f"Somatorio das notas: {soma}")
print(f"Média do aluno: {media:.1f}")
if media >= 6:
        print("Aprovado")
        print("Parabéns :)")
elif media < 3.9:
    print("Reprovado")
    print("Tê vejo ano que vem ;)")
else: 
    print("Recuperação")
    print("Tê vejo em breve ;)")