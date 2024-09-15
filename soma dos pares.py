numero = int(input("Digite um número: "))
soma_pares = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        soma_pares += i
print("A soma dos números pares entre 1 e", numero, "é:", soma_pares)
