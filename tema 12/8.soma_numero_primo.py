soma_primos = 0  # Inicia a soma dos numeros primos

for numero in range(1, 101):
    #faz o calculo do numero primo
    primo = True
    if numero < 2:
        primo = False
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                primo = False
                break
    if primo:
        soma_primos = soma_primos + numero  # Adiciona um numero primo a soma

print("A soma de todos os números primos entre 1 e 100 é:", soma_primos)
