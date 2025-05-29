cont = 0
soma = 0

while True:
    n = int(input('Digite o numero para media de pares (digite 0 para o resultado/sair): '))

    if n == 0:
        break
    if n %2 == 0:
        soma = soma + n 
        cont = cont + 1
if cont == 0:
    print('Nenhum numero par foi digitado.')
else:
    media = soma / cont
    print('A media dos numeros pares é: ', media)
