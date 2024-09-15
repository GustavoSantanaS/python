val = []

n = int(input("Quantos valores você deseja inserir? "))

for i in range(n):
    valor = int(input("Digite o valor " + str(i+1) + ": "))
    val.append(valor)

maior = val[0]
menor = val[0]

for valor in val:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

diferenca = maior - menor

print("A diferença entre o maior e o menor valor é:", diferenca)
