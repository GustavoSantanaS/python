# aqui e colocado para o usuario declarar o valor das variaveis
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
#aqui e declarado o valor da variavel C
C = 10 , 2, 6 , 2, 15 , 3

# aqui e feito um loop até que A seja menor ou igual a B
while A > B:
#aqui e feito a subtraçao de A e B
    A -= B
#aqui e feito a soma de C
soma = sum(C)

#aqui mostra os valores finais de C e A
print("O valor final de C é: " , soma)
print("O valor final de A é: ", A)
