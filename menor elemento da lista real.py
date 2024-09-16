# Lista com numeros reais
numeros = [3.5, 2.1, 4.7, 1.2, 5.9]

# Começa o menor valor e o índice
menor = numeros[0]
indice = 0

# Percorrer a lista para encontrar o menor valor e sua posição
for i in range(1, len(numeros)):
    if numeros[i] < menor:
        menor = numeros[i]
        indice = i

# Mostrar os resultados na tela
print("O menor elemento da lista é", menor, " e sua posição (índice) é", indice)
