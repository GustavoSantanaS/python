valor_conta = int(input("Digite o valor da conta: "))

notas_50 = valor_conta // 50
valor_conta %= 50

notas_10 = valor_conta // 10
valor_conta %= 10

notas_1 = valor_conta
print("Serão necessarias")
print("Notas de 50:", notas_50)
print("Notas de 10:", notas_10)
print("Notas de 1:", notas_1)
