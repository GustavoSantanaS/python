#variavel com o comeco com cada numero
maior = -0 
menor = 0
cont = 1

while True: #inicia o loop com entrada de dados do usuario
    n = int(input('Digite um número inteiro (digite 0 para sair): '))
    if n == 0:
        break
    if cont == 1: # ve se e a primeira interacao do loop
        maior = n
        menor = n
        cont = 0  #da uma atualizada no cont para não entrar mais nesta condição
    if n > maior: #verifica se e maior
        maior = n 
    if n < menor: #ve se e menor
        menor = n

if maior and menor: # ve o maior e o menor se foram atualizados de acordo com a resposta do usuario
    print('O maior número foi', maior)
    print('O menor número foi', menor)
else:
    print('Nenhum número válido foi digitado.')
