soma_primos = 0  # Inicia a soma dos numeros primos

for n in range(1, 101):
    #faz o calculo do numero primo
    primo = True
    if n < 2:
        primo = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                primo = False
                break
    if primo:
        soma_primos = soma_primos + n  # Adiciona um numero primo a soma

print("A soma de todos os números primos entre 1 e 100 é:", soma_primos)
