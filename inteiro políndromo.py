numero = input("Digite um número inteiro: ")
palindromo = True

for i in range(len(numero) // 2):
    palindromo = palindromo and (numero[i] == numero[-i-1])

mensagem = "é um palíndromo." if palindromo else "não é um palíndromo."
print(numero, mensagem)
