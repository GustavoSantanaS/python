numero = input("Digite um número inteiro: ")

if numero == numero[::-1]:
    print(numero, "é um palíndromo.")
else:
    print(numero, "não é um palíndromo.")
